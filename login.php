<?php
if (isset($_POST['login'])) {
  $email = $_POST['email'];
  $password = $_POST['password'];
  
  header("Location: welcome.php");
  exit();
}
?>
