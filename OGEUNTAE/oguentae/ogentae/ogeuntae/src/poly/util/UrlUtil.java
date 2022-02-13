package poly.util;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.net.URL;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


// url 접속을 통해 Text 내용 읽어오는 역할 수행하는 클래스
public class UrlUtil {
	private final Logger log = LoggerFactory.getLogger(this.getClass());
	
	private String readAll(Reader rd) {
		log.info(this.getClass() + "readAll Start !!");
		
		StringBuilder sb = null;
		
		try {
			sb = new StringBuilder();
			int cp = 0;
			
			while((cp = rd.read()) != -1) {
				sb.append((char) cp);
				//log.info("cp " + (char)cp);
			}
		} catch (Exception e) {
			log.info("readAll Exception : " + e.toString());
		}
		log.info("readAll END!!!");
		return sb.toString();
	}
	
	public String urlReadforString(String url) throws IOException{
		log.info("url Read for String Strart!!");
		log.info("url Read for String url : " + url);
		
		BufferedReader rd = null;
		InputStream is = null;
		String res = "";
		
		try {
			is = new URL(url).openStream();
			// URL 결과 내용이 많을 수 있어서 버퍼 사용
			rd = new BufferedReader(new InputStreamReader(is));
			// 결과 가져오기
			res = readAll(rd);
			log.info("res :: "+ res);
		}catch (Exception e) {
			log.info("URL readforString Exception : " + e.toString());
		} finally {
			is.close();
			is = null;
			rd = null;
		}
		
		log.info("url Rad fot String End!!");
		return res;
	}

}
