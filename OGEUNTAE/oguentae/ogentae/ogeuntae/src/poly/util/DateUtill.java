package poly.util;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
// 오늘 날짜를 반환해주는 메서드
public class DateUtill {
	/**
	 * 날짜, 시간 출력하기
	 * 
	 * @param fm 날짜 출력 형식
	 * @return
	 */
	public static String getDateTimeAdd(int day) {

		return getDateTimeAdd("yyyyMMdd", day);

	}
	
	public static String getDateTimeAdd(String fm, int day) {

		SimpleDateFormat date = new SimpleDateFormat(fm);

		Calendar cal = Calendar.getInstance();
//        cal.add(Calendar.DATE, day-1);		//장애 대응용
		cal.add(Calendar.DATE, day);

		return date.format(cal.getTime());

	}
	
	// 포맷을 지정하면 지정한 대로
	public static String getDateTime(String fm) {
	Date today = new Date();
	System.out.println(today);
	
	SimpleDateFormat date = new SimpleDateFormat(fm);
	
	return date.format(today);
	}
	// 오버로딩을 활용하여 함수 구현 지정 안하면 아래 형식으로
	public static String getDateTime() {
		return getDateTime("yyyy.MM.dd");
	}
	
}
