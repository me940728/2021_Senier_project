package poly.util;

import org.apache.log4j.Logger;

public class TestDum {
	
	Logger log = Logger.getLogger(this.getClass());

	public static void main(String[] args) {
		String pLateTime = "21:30";
		String pEmpTime = "2021_06_02_20:30";
		
		String res = JsonParsProc.lateCheck(pEmpTime, pLateTime);
		
		System.out.println(res);
	}
	
}
