<?php
session_start();
if(session_destroy()){ // Destroy All Sessions 
header("Location: index.php"); // Redirecting To Home Page
}
?>