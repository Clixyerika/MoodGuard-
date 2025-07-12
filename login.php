<?php
require 'db.php';

$username = $_POST['username'];
$password = $_POST['password'];

$sql = "SELECT * FROM users WHERE username = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("s", $username);
$stmt->execute();
$result = $stmt->get_result();
$user = $result->fetch_assoc();

if ($user && password_verify($password, $user['password'])) {
  echo json_encode(["status" => "success", "message" => "Login successful."]);
} else {
  echo json_encode(["status" => "error", "message" => "Invalid credentials."]);
}
?>