<!DOCTYPE HTML>
<html>
 <head>
 <link href="http://designmodo.github.io/Flat-UI/bootstrap/css/bootstrap.css" rel="stylesheet">
 <link href="http://designmodo.github.io/Flat-UI/css/flat-ui.css" rel="stylesheet">
 <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
 </head>
 <body>
 	<div class="container">
 		<div class="title">{{filename}}</div>
 		<div class="data">{{content}}</div>
 		<div class="row">
 			<button id="btn-change" onclick="changeFile()" class="btn btn-primary">换一批</button>
 		</div>
 	</div>
 </body>
  <style type="text/css">
 @media (min-width: 1200px) { .container{ width: 2170px;}}
 </style>
 </html>