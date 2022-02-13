<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%
    String empno = (String)request.getAttribute("empno");
    String aemail= (String)session.getAttribute("aemail");
    %>
   <%
    if(aemail == null){
    	response.sendRedirect("/user/sessioCheck.do");	
    }
    %>
<!DOCTYPE html>
<html>
<head>
<style type="text/css">
* {
	font-size: 25px;
	font-family: Consolas, sans-serif;
	background-color: #c3cdda;
	text-align: center;
}
.substyle{
background-color: white;
border-radius: 5px;
}
</style>
<meta charset="UTF-8">
<title>imgStorageJAVA</title>
    <link rel="stylesheet" href="/resources/webCam/stylesheets/main.css">
</head>
<body>
<input type='button' onclick='javascript()' value='사진촬영' class="substyle"/>

      <div class="booth">
          <video id="video" width="800" height="600" autoplay=""></video>
          <canvas id="canvas" width="800" height="600"></canvas>
          <a onclick=windows.close()></a>
      </div>
      
      <script src="/resources/webCam/javascripts/video.js"></script>
      
      <script>
      function javascript(){
    	    //현재창에서 다른페이지로 이동
    	    window.location.href="imgStorageProc.do?empno=<%=empno%>";
    	}
      </script>                        
</body>
</html>