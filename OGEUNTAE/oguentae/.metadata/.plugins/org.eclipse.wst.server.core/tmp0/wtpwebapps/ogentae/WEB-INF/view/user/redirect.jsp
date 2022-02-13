<%@page import="poly.util.CmmUtil"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%
	String msg = CmmUtil.nvl((String)request.getAttribute("msg"));
	String url = CmmUtil.nvl((String)request.getAttribute("url")) ;
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>REDIRECT</title>

<script type="text/javascript">
alert("<%=msg%>")
location.href = "<%=url%>"
</script>
