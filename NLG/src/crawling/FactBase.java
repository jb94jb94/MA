package crawling;
 import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.net.SocketTimeoutException;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

public class FactBase {

	public static void main(String[] args) throws Exception {
		String date = "2020-02-28";
		int noSpeeches = 1;
		String link;
		for (int i = 1; i < 200; i++) {
			String doc = Jsoup
					.connect("https://factba.se/json/json-transcript.php?f=&start_date=2010-01-01&end_date=" + date)
					.ignoreContentType(true).timeout(0).validateTLSCertificates(false).execute().body();
			JsonParser parser = new JsonParser();
			JsonObject rootObj = parser.parse(doc).getAsJsonObject();
			JsonArray data = rootObj.getAsJsonArray("data");
			for (JsonElement entry : data) {
				if (((JsonObject) entry).get("type").getAsString().equals("Speech")) {
					link = ((JsonObject) entry).get("slug").getAsString();
					System.out.println(noSpeeches + ": " + link);

					boolean read = false;
					int tries = 0;
					while (!read) {
						tries++;
						if (tries > 1) {
							System.out.println("tries: " + tries);
						}
						if (tries > 3) {
							throw new Exception();
						}
						try {
							Document speech = Jsoup.connect("https://factba.se/transcript/" + link).timeout(0)
									.ignoreContentType(true).validateTLSCertificates(false).get();

 							JsonObject speechObj = parser
									.parse(speech.selectFirst("script[type='application/ld+json']").html())
									.getAsJsonObject();
							String content = speechObj.get("articleBody").getAsString();
							System.out.println(content.substring(0, 100));
							BufferedWriter writer = new BufferedWriter(
									new FileWriter(new File("Factbase/text/" + noSpeeches + ".txt")));

							JsonObject joText = new JsonObject();
							joText.addProperty("id", i);
							joText.addProperty("author", "Donald Trump");
							joText.addProperty("title", ((JsonObject) entry).get("record_title").getAsString());
							joText.addProperty("date", ((JsonObject) entry).get("date").getAsString());
							content = content.replaceAll("\\[[^\\]]*]", " ");
							content = content.replaceAll(" +", " ");
							joText.addProperty("text", content);
							writer.write(joText.toString());
							writer.flush();
							writer.close();
							noSpeeches++;
							read = true;
						} catch (SocketTimeoutException ste) {
						}
					}
				}
				date = ((JsonObject) entry).get("date").getAsString();
			}
		}
	}
}
