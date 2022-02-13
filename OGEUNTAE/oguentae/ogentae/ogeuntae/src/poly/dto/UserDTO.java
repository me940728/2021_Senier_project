package poly.dto;

/**
 * @author 최별규
 * @version 1.1 로그인 + 회원가입 DTO
 */
public class UserDTO {

	private int ano; // 관리자 번호
	private String aname; // 관리자 이름
	private String aemail; // 관리자 아이디(이메일)
	private String apw; // 비밀번호
	private String reg_dt; // 가입일
	private String chg_dt; // 수정일
	private String exists_yn; // 이메일 중복 확인
	
	public int getAno() {
		return ano;
	}
	public void setAno(int ano) {
		this.ano = ano;
	}
	public String getAname() {
		return aname;
	}
	public void setAname(String aname) {
		this.aname = aname;
	}
	public String getAemail() {
		return aemail;
	}
	public void setAemail(String aemail) {
		this.aemail = aemail;
	}
	public String getApw() {
		return apw;
	}
	public void setApw(String apw) {
		this.apw = apw;
	}
	public String getReg_dt() {
		return reg_dt;
	}
	public void setReg_dt(String reg_dt) {
		this.reg_dt = reg_dt;
	}
	public String getChg_dt() {
		return chg_dt;
	}
	public void setChg_dt(String chg_dt) {
		this.chg_dt = chg_dt;
	}
	public String getExists_yn() {
		return exists_yn;
	}
	public void setExists_yn(String exists_yn) {
		this.exists_yn = exists_yn;
	}
	
	
}
