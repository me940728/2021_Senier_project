<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%
    String apiURL = (String)request.getAttribute("apiURL");
    %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>API URL</title>
</head>
<body>
<script type="text/javascript">
location.href="<%=apiURL%>";
</script>
</body>
</html>