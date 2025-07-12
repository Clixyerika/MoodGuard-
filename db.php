<?php
$host = "localhost";     // your DB host
$user = "root";          // DB username
$pass = "";              // DB password
$db   = "moodguard";     // DB name

$conn = new mysqli($host, $user, $pass, $db);

if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
?>