<?php 

//include database configuration
include 'includes/config.php';

// Turn off error reporting
error_reporting(0);

//start the session
session_start();


if (isset($_POST['submit'])) {
	$username = $_POST['username'];
	$email = $_POST['email'];
	$password = md5($_POST['password']); //hash function
	$cpassword = md5($_POST['cpassword']);

	//if the cpassword is correct complete the registration or reinsert the information in the form
	if ($password == $cpassword) 
	{
	// unique name and e-mail for each user
		$sql = "SELECT * FROM users WHERE email='$email'or username='$username'";
		$result = mysqli_query($conn, $sql);

		if (!$result->num_rows > 0)
		{
			$sql = "INSERT INTO users (username, email, password)
					VALUES ('$username', '$email', '$password')";
			$result = mysqli_query($conn, $sql);

			if ($result)
			{
				echo "
				<script>
					alert('Registration completed successfully');
					alert('Please return to the sign in page');
				</script>";
				
			} 
			
			else 
			{
				echo "
				<script>
					alert('Warning! Something Wrong Went, please try again');
				</script>";
			}

		}
		else 
		{
			echo "
			<script>
				alert('Warning! Email or username Already Exists.');
			</script>";
		}
		
	} 
	
	else 
	{
		echo 
		"<script>
			alert('Warning! Password Not Matched.')
		</script>";
	}
}

?>

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Sign up</title>
</head>

<body>
	<!-- header-->
	<?php include 'includes/header-login.php' ?>

	<section class="container">
		<form action="" method="POST" class="login">
		<!--login header -->
            <p class="login-text">Create Account</p>

		<!-- inputs for registration-->
			<div class="input-form">
				<label for="username">Username</label>
				<input type="text" placeholder="Username" name="username" id="username" value="<?php echo $username; ?>" required><!--replir le champ avans l'envoi du formulaire  -->
 			</div>

			<div class="input-form">
				<label for="email">Email</label>
				<input type="email" placeholder="Email" name="email" id="email" value="<?php echo $email; ?>" required>
			</div>

			<div class="input-form">
				<label for="password">Password</label>
				<input type="password" placeholder="Password" name="password" id="password" value="<?php echo $_POST['password']; ?>" required>
            </div>

            <div class="input-form">
				<label for="cpassword">Confirm password</label>
				<input type="password" placeholder="Confirm Password" name="cpassword" value="<?php echo $_POST['cpassword']; ?>" required>
			</div>

			<!-- submit button-->
			<div class="input-form">
				<button name="submit" class="btn">Sing up</button>
			</div>

			<!-- link to sing in -->
			<p class="login-register-text">Have you an account? <a href="SignIn.php">Sing in</a>.</p>
		</form>
	</section>

	<!--footer-->
	<?php include 'includes/footer.php'?>

</body>
</html>