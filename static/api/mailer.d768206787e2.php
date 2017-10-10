<?php
$name = $_POST['name'];
$email = $_POST['email'];
$message = $_POST['message'];
 
$to = 'yourdomain@host.com';
$subject = 'the subject';
$message = 'FROM: '.$name.' EMAIL: '.$email.' MESSAGE: '.$message;
$headers = 'From: '. $email. "\r\n";

mail($to, $subject, $message, $headers); 
echo "Thanks, your email was sent!";
?>