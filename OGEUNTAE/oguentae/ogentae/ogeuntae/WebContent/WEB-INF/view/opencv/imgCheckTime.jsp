<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
	
	
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>imgCheckTime</title>
<style>
	* {
		font-size: 25px;
		font-family: Consolas, sans-serif;
		background-color: #c3cdda;
		text-align: center;
	}
	
	form {
		margin: 0 auto;
		width: 250px;
	}
	
	.substyle{
	background-color: white;
	border-radius: 5px;
	}
</style>
</head>

<body>
	<h1>출석 확인 종료시간을 입력해 주세요.</h1>
	<form action="/imgCheckTest.do">
		<p>
		<span>지각 시간</span>
		<input type="time" id="lateTime" name="lateTime" class="substyle">
		</p>
		
		<p>
		<span>종료 시간</span>
			<input type="time" id="time" name="time" class="substyle">
		</p>
		<p>
			<input type="submit" value="완료" class="substyle">
		</p>

	</form>
	
	<script type="text/javascript">
	      function javascript(){
    	    //현재창에서 다른페이지로 이동
    	    window.location.href="imgCheckTime.do?ascTime=<%="27"%>";
		}
	</script>
</body>
</html>