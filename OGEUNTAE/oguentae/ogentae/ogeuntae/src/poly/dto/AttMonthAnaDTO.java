package poly.dto;
// 년도 별 월 지각자 수 분석을 위한 DTO
public class AttMonthAnaDTO {
	
	private String month; // 집계 월
	private String late_CheckCount; // 지각 수 체크

	public String getMonth() {
		return month;
	}
	public void setMonth(String month) {
		this.month = month;
	}
	public String getLate_CheckCount() {
		return late_CheckCount;
	}
	public void setLate_CheckCount(String late_CheckCount) {
		this.late_CheckCount = late_CheckCount;
	}
	
	
	
}
