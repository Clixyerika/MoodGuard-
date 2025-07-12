<?php
require 'db.php';

$username = $_POST['username'];
$password = password_hash($_POST['password'], PASSWORD_DEFAULT);
$email    = $_POST['email'];

$sql = "INSERT INTO users (username, email, password) VALUES (?, ?, ?)";
$stmt = $conn->prepare($sql);
$stmt->bind_param("sss", $username, $email, $password);

if ($stmt->execute()) {
  echo json_encode(["status" => "success", "message" => "User registered successfully."]);
} else {
  echo json_encode(["status" => "error", "message" => "Username or email already exists."]);
}
?>