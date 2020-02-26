<?php
session_start();
if(session_unset()){ // Unset All Sessions 
header("Location: index.php"); // Redirecting To Home Page
}
?>