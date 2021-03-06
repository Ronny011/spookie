<?php
include('login.php'); // Includes Login Script
if(isset($_SESSION['login_user'])){
header("location: profile.php"); // Redirecting To Profile Page
}
?>
<!-- Form-->
<link href="Login.css" rel="stylesheet" type="text/css">
<link href="external.css" rel="stylesheet" type="text/css">
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
<script src="Login.js"></script>

<body>

  <div class="form">
    <div class="form-toggle"></div>
    <div class="form-panel one">
      <div class="form-header">
        <h1>Account Login</h1>
      </div>
      <div class="form-content">
        <form action="" method="post">
          <div class="form-group">
            <label for="username">Username</label>
            <input type="text" id="username" name="username" required="required" />
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" id="password" name="password" required="required" />
          </div>
          <div class="form-group">
          </div>
          <div class="form-group">
            <input name="submit" type="submit" value=" Login ">
            <span><?php echo $error; ?></span>
          </div>
        </form>
      </div>
    </div>
    <div class="form-panel two">
      <div class="form-header">
        <h1>Register Account</h1>
      </div>
      <div class="form-content">
        <form>
          <div class="form-group">
            <label for="username">Username</label>
            <input type="text" id="username" name="username" required="required" />
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" id="password" name="password" required="required" />
          </div>
          <div class="form-group">
            <label for="cpassword">Confirm Password</label>
            <input type="password" id="cpassword" name="cpassword" required="required" />
          </div>
          <div class="form-group">
            <button type="submit">Register</button>
          </div>
        </form>
      </div>
    </div>
  </div>
  <div class="pen-footer"><a target="_blank">Ronny Paz</a><a target="_blank">Liron Glickman</a></div>
</body>