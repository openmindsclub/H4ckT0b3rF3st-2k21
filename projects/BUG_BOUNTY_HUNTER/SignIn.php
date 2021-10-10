<?php 

include 'includes/config.php';

session_start();

error_reporting(0);

if (isset($_SESSION['username'])) {
    header("Location: home.php");
}

if (isset($_POST['submit'])) {
	$username = $_POST['username'];
	$password = md5($_POST['password']);

	$sql = "SELECT * FROM users WHERE username='$username' AND password='$password'";
	$result = mysqli_query($conn, $sql);
	if ($result->num_rows > 0) {
		$row = mysqli_fetch_assoc($result);
		$_SESSION['username'] = $row['username'];
		header("Location: home.php");
		
	}
	else {
		echo "
		<script>
			alert('warning! Email or Password is Wrong.')
		</script>";
	}
}

?>

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Sign In</title>
</head>
<body>

	<!-- header -->
	<?php include 'includes/header-login.php' ?>
	
	<!--sign in section--> 
	<section class="container">
		<form action="" method="POST" class="login">
			<p class="login-text" >Sign In</p>
			<div class="input-form">
				<label for="username">Username </label>
				<input type="username" placeholder="username" id="username" name="username" value="<?php echo $username; ?>" required>
			</div>
			<div class="input-form">
				<label for="password">Password</label>
				<input type="password" placeholder="Password" name="password" id="password" value="<?php echo $_POST['password']; ?>" required>
			</div>
			<div class="input-form">
				<button name="submit" class="btn">Login</button>
			</div>
			<p class="login-register-text">Don't have an account? <a href="SignUp.php"> Sing up</a>.</p>
		</form>
	</section>

	<!--footer-->
	<?php include 'includes/footer.php'?>

</body>
</html>