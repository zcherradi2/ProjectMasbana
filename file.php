<?php
$con=mysqli_connect("localhost","root","","users_db");
if (mysqli_connect_errno($con)) {
echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
$username = $_GET['username'];
$password = $_GET['password'];
$result = mysqli_query($con,"SELECT Username FROM users where Username='$username'
and Password='$password'");
$row = mysqli_fetch_array($result);
$data = $row[0];
if($data){
echo "$data authorized";
}
else
{
echo "invalid account";
}
mysqli_close($con);
?>