<?php

var_dump($_POST);
$email = "";
$MAC = "";
if (isset($_POST['email'])) {
    $email = $_POST['email'];
    echo "$email";
}

if (isset($_POST['MAC'])) {
    $MAC = $_POST['MAC'];
    echo "$MAC";
}

$myArr = array($email, $MAC);
$json = json_encode($myArr);
$file = 'myjson.json';

file_put_contents($file, $json);
?>

