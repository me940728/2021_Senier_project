package poly.service;

import java.io.IOException;
import java.util.List;

import poly.dto.EmpAttDTO;

public interface IEmpAttService {

	int empAttProc(String addres, String checktime, String ascTime, String lateTime) throws IOException, Exception;

}
