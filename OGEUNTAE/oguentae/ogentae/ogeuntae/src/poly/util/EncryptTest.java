package poly.util;

public class EncryptTest {

	public static void main(String[] args) throws Exception{
		
		System.out.println("start");
		System.out.println("해시 알고리즘");
		
		//암호화 문자열
		String str ="1234";
		
		//복호화가 불가능한 해시함호화 알고리즘 실행
		String hashEnc = EncryptUtil.encHashSHA256(str);

		//해쉬 암호화 알고리즘 결과 출력
		System.out.println("hashEnc : "+hashEnc);
		
		System.out.println("and");
		System.out.println("AES128-CBC 암, 복호화 알고리즘");
		
		String enc = EncryptUtil.encAES128CBC(str);
		
		System.out.println("enc :"+enc);
		
		String dec = EncryptUtil.decAES128CBC(enc);
		
		System.out.println("dec : "+dec);
		System.out.println("end");
		// 메일 랜덤 문자 발송용 메서드 테스트
		System.out.println(RamdomMail.SendRamdomMail());
	
	}
}
	