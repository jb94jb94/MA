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

		// boolean skip = true;
		int i = 0;

		String date = "";
		// for (Element href : doc.select("[href]")) {
		for (Element tr : doc.select("tr")) {
			// if (!k) {
			if (tr.selectFirst("[face='Tahoma']") != null
					&& tr.selectFirst("[face='Tahoma']").select("[size='4']") != null) {
				date = tr.selectFirst("[face='Tahoma']").select("[size='4']").text();
				if (!date.equals("")) {
					Element href = tr.selectFirst("[href]");
					if (href != null && href.text() != null) {
						if (href.toString().contains(".htm") && !href.text().contains("PDF")) {
							i++;
							if (i % 20 == 0) {
								System.out.println(i);
							}
							String link = "https://americanrhetoric.com/" + href.attr("href");

							Document speech = Jsoup.connect(link).validateTLSCertificates(false).get();
							for (Element sup : speech.select("[color='#FF0000']")) {
								sup.remove();
							}
							BufferedWriter writer = new BufferedWriter(
									new FileWriter(new File("AmRhet/text/" + i + ".txt")));
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
							
							writer.flush();
							writer.close();
						}
					}
				}
			}
		}
	}
}
