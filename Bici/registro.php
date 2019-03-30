<!DOCTYPE html>
<html lang="en">
<head>
  <title>Registro</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
   <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <style>
  .fakeimg {
    height: 200px;
    background: #aaa;
  }
  </style>
</head>

<body>
    <div class="card bg-light">
<article class="card-body mx-auto" style="max-width: 400px;">
    <h4 class="card-title mt-3 text-center">Create Account</h4>
    <p class="text-center">Get started with your free account</p>

    <form action="" method="get">
    <div class="form-group input-group">
        <div class="input-group-prepend">
            <span class="input-group-text"> <span class="glyphicon glyphicon-user"></span></span>
         </div>
        <input name="nameC" class="form-control" placeholder="Full name" type="text">
    </div> <!-- form-group// -->
    <div class="form-group input-group">
        <div class="input-group-prepend">
            <span class="input-group-text"> <span class="glyphicon glyphicon-envelope"></span></span>
         </div>
        <input name="emailC" class="form-control" placeholder="Email address" type="email">
    </div> <!-- form-group// -->
    <div class="form-group input-group">
        <div class="input-group-prepend">
            <span class="input-group-text"> <span class="glyphicon glyphicon-phone"></span></span>
        </div>
        <input name="telNumber" class="form-control" placeholder="Phone number" type="text">
    </div> <!-- form-group// -->
    <div class="form-group input-group">
        <div class="input-group-prepend">
            <span class="input-group-text"> <span class="glyphicon glyphicon-phone"></span></span>
        </div>
        </div>
        <input name="direccionC" class="form-control" placeholder="direccionC" type="text">
    </div> <!-- form-group// -->
    <div class="form-group input-group">
        <div class="input-group-prepend">
            <span class="input-group-text"> <span class="glyphicon glyphicon-lock"></span></span>
        </div>
        <input name = "passwordC" class="form-control" placeholder="Create password" type="password">
    </div> <!-- form-group// -->
    <div class="form-group input-group">
        <div class="input-group-prepend">
            <span class="input-group-text"> <span class="glyphicon glyphicon-lock"></span></span>
        </div>
        <input name = "passwordCrep" class="form-control" placeholder="Repeat password" type="password">
    </div> <!-- form-group// -->                                      
    <div class="form-group">
        <button type="success" class="btn btn-success btn-block"> Create Account</button>
    </div> <!-- form-group// -->      
    <p class="text-center">Have an account? <a href="index.html">Log In</a> </p>                                                                 
</form>
</article>

</div> 
</body>
</html>
<style type="text/css">
    .divider-text {
    position: relative;
    text-align: center;
    margin-top: 15px;
    margin-bottom: 15px;
}
.divider-text span {
    padding: 7px;
    font-size: 12px;
    position: relative;   
    z-index: 2;
}
.divider-text:after {
    content: "";
    position: absolute;
    width: 100%;
    border-bottom: 1px solid #ddd;
    top: 55%;
    left: 0;
    z-index: 1;
}

.btn-facebook {
    background-color: #405D9D;
    color: #fff;
}
.btn-twitter {
    background-color: #42AEEC;
    color: #fff;
}
</style>

<?php
$nameC = $_GET['nameC'];
$db = new SQLite3('estatal.db');
$sql = "INSERT INTO ciclista (nombre_ciclista, direccion, telefono, correociclista, contrasenaciclista) VALUES('$nameC', 'Rusia o algo, yo que se', '555-NUMERO-NO-DETERMINISTA', 'markov@example.com', '123');";
$result = $db->query($sql);
unset($db);
?>