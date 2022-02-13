package poly.controller;

import java.util.List;

import javax.annotation.Resource;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

import org.apache.log4j.Logger;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

import poly.dto.EmpDTO;
import poly.dto.MailDTO;
import poly.service.IEmpService;
import poly.service.IMailService;
import poly.util.CmmUtil;

@Controller
public class SendMailController {

	// 로거
	Logger log = Logger.getLogger(this.getClass());
	
	@Resource(name = "EmpService")
	IEmpService empService;
	
	@Resource(name = "MailService")
	IMailService mailService;
	

	// 메일 발송 매핑
	@RequestMapping(value="sendMail") //.do 입력
	public String SendMail(Model model) {
		log.info(this.getClass());
		
		List<EmpDTO> rList = empService.getEmpList(); 
		
		for(EmpDTO e : rList) {
			log.info("ENAME : " + e.getEname());
			log.info("EEMAIL : " + e.getEemail());
		}
		
		model.addAttribute("rList", rList);
		
		log.info(this.getClass());
		return "/mainPage/sendMail";
	}
	
	// 이미지 저장을 위한 매핑
	@RequestMapping(value="sendMailProc") // .do
	public String imgStorage(HttpServletRequest request, Model model, HttpSession session) {
		log.info("send email Proc start!!");
		
		String eemail = CmmUtil.nvl(request.getParameter("eemail"));; // JSP 직원 선택 한 값을 가져오기
		String title = CmmUtil.nvl(request.getParameter("title"));
		String contents = CmmUtil.nvl(request.getParameter("contents"));
		String msg = "";
		String url = "";
	
		MailDTO mDTO = new MailDTO();
		
		mDTO.setToMail(eemail);
		mDTO.setTitle(title);
		mDTO.setContents(contents);
		
		int res = mailService.doSendMail(mDTO);
		
		if(res > 0) {
			log.info("메일 발송 성공 res 1 == " + res);
			msg = "메일 발송이 완료되었습니다.";
			url = "/sendMail.do";
		} else {
			log.info("메일 발송 실패 res 0 == " + res);
			msg = "메일 발송이 실패하였습니다.";
			url = "/sendMail.do";
			
		}	
		
		model.addAttribute("msg", msg);
		model.addAttribute("url", url);
		
		log.info("send email Proc end!!");
		 mDTO = null;
		 
		return "/user/redirect";
	}
		
	
	
}
