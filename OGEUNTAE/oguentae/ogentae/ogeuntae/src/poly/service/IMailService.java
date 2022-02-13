package poly.service;

import poly.dto.MailDTO;

public interface IMailService {
	// 메일 전송 DTO
	int doSendMail(MailDTO pDTO);

}
