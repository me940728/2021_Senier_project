package poly.service;

import java.util.List;

import poly.dto.AttAnalysDTO;
import poly.dto.AttMonthAnaDTO;

public interface IAttAnalysService {
	// 분석을 위한 직원 정보 불러오기
	List<AttAnalysDTO> getAttInfo();
	// 직원 총인원 구하는 메서드
	AttAnalysDTO getEmpCount();
	// 몽고에서 데이터 가죠오는 메서드
	public List<AttAnalysDTO>  selectAttInfoForMongo() throws Exception;
	// 몽고에서 분석을 위해 데이터를 가져옴
	public List<AttMonthAnaDTO> getAttMonthAna() throws Exception;

}
