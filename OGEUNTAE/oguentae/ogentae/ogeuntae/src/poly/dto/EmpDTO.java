package poly.dto;


public class EmpDTO {
	
	private String empno; // 직원번호
	private String ename; // 직원이름
	private String bday; // 생년월일
	private String sex; // 성별
	private String eemail; // 직원 이메일
	private String pro_Image; // 대표사진
	private String inAdmin; // 등록한 관리자
	private String upAdmin; // 수정한 관리자
	private String addrs; // 주소
	private String att_date; // 출석시간 
	private String exists_yn; // 이메일 중복 확인
	
	public String getEmpno() {
		return empno;
	}
	public void setEmpno(String empno) {
		this.empno = empno;
	}
	public String getEname() {
		return ename;
	}
	public void setEname(String ename) {
		this.ename = ename;
	}
	public String getBday() {
		return bday;
	}
	public void setBday(String bday) {
		this.bday = bday;
	}
	public String getSex() {
		return sex;
	}
	public void setSex(String sex) {
		this.sex = sex;
	}
	public String getEemail() {
		return eemail;
	}
	public void setEemail(String eemail) {
		this.eemail = eemail;
	}
	public String getProImage() {
		return pro_Image;
	}
	public void setProImage(String proImage) {
		this.pro_Image = proImage;
	}
	public String getInAdmin() {
		return inAdmin;
	}
	public void setInAdmin(String inAdmin) {
		this.inAdmin = inAdmin;
	}
	public String getUpAdmin() {
		return upAdmin;
	}
	public void setUpAdmin(String upAdmin) {
		this.upAdmin = upAdmin;
	}
	public String getAddrs() {
		return addrs;
	}
	public void setAddrs(String addrs) {
		this.addrs = addrs;
	}
	public String getAttDate() {
		return att_date;
	}
	public void setAttDate(String att_date) {
		this.att_date = att_date;
	}
	public String getExists_yn() {
		return exists_yn;
	}
	public void setExists_yn(String exists_yn) {
		this.exists_yn = exists_yn;
	}
	
}

