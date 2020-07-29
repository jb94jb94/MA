package crawling;
 import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;

import com.google.gson.JsonObject;

public class AmericanRhetoric {

	public static void main(String[] args) throws IOException {

		Document doc = Jsoup.connect("https://americanrhetoric.com/barackobamaspeeches.htm")
				.validateTLSCertificates(false).get();

		int i = 0;
		String date = "";
		
		for (Element tr : doc.select("tr")) {
			if (tr.selectFirst("[face='Tahoma']") != null
					&& tr.selectFirst("[face='Tahoma']").select("[size='4']") != null) {
				date = tr.selectFirst("[face='Tahoma']").select("[size='4']").text();
				if (!date.equals("")) {
					System.out.println(date);
					Element href = tr.selectFirst("[href]");
					if (href != null && href.text() != null) {
						if (href.toString().contains(".htm") && !href.text().contains("PDF")) {
							System.out.println(href.text());
							i++;
							if (i % 20 == 0) {
								System.out.println(i);
							}
							String link = "https://americanrhetoric.com/" + href.attr("href");

							Document speech = Jsoup.connect(link).validateTLSCertificates(false).get();
							for (Element sup : speech.select("[color='#FF0000']")) {
								sup.remove();
							}
							BufferedWriter writer = new BufferedWriter(new FileWriter(new File("AmRhet/text/" + i + ".txt")));
							StringBuilder sb = new StringBuilder();
							boolean found = false;

							for (Element e : speech.select("[style^='line-height:']")) {
								if (!e.text().isEmpty()) {
									found = true;
									sb.append(e.text() + "\n");
								}
							}
							if (!found) {
								for (Element e : speech.select("[face='Verdana']")) {
									if (!e.text().isEmpty() && !e.text().contains("Book/CD") && !e.text().contains(
											"[AUTHENTICITY CERTIFIED: Text version below transcribed directly from audio]")
											&& !e.text().contains("[text unauthenticated]")) {
										found = true;
										sb.append(e.text() + "\n");
									}
								}
							}
							
							JsonObject joText = new JsonObject();
							joText.addProperty("id", i);
							joText.addProperty("author", "Barack Obama");
							joText.addProperty("title", href.text());
							joText.addProperty("date", date);
							
							String content = sb.toString();
							
							content = content.replaceAll("\\[[^\\]]*]", " ");
							content = content.replaceAll(" +", " ");
							joText.addProperty("text", content);
							
							writer.write(joText.toString());
							writer.flush();
							writer.close();
						}
					}
				}
			}
		}
	}
}
