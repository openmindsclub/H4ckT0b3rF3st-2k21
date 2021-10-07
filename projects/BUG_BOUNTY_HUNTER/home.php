<?php 

session_start();

if (!isset($_SESSION['username'])) {
    header("Location: index.php");
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>C-readers</title>
</head>
<body>
    <?php include 'includes/header-logout.php' ?>

    <p class="welcome">
        <?php echo "<b>  Welcome, " . $_SESSION['username'] . " ! <b>"; ?>
    </p>

    <hr>

    <h1>Book List</h1>

    <section>
        <div class="container">

            <div class="card">
                <div class="imgBox">
                    <img src="img/7.jpg" alt="Aya Kito book">
                 </div> 
                    <div class="details">
                        <q>Don't worry, even if you fall over! It's all right. You can just pick yourself up again! When you fall over, make the most of the chance to look up and see the sky. You will see the blue sky spreading endlessly above you and smiling down. Aya, you are alive!</q>
                        <br> <br>
                        <cite>- Aya Kito, 1 Litre of Tears</cite>
                    </div>
             </div> 

            <div class="card">
                <div class="imgBox">
                    <img src="img/5.jpg" alt="Mourid Barghouti book">
                 </div> 
                    <div class="details">
                        <q>The homeland does not leave the body until the last moment, the moment of death. The fish, Even in the fisherman's net,Still carries the smell of the sea</q>
                        <br> <br>
                        <cite>- Mourid Barghouti, I Saw Ramallah</cite>
                    </div>
            </div> 
    
            <div class="card">
                <div class="imgBox">
                    <img src="img/1.jpg" alt="dan brown book">
                 </div> 
                <div class="details">
                        <q>When a computer creates art, who is the artist—the computer or the programmer?</q>
                        <br> <br>
                        <cite>- Origin, Dan BROWN</cite>
                </div>
            </div> 

            <div class="card">
                <div class="imgBox">
                    <img src="img/6.jpg" alt="Ghassan kanafani book">
                 </div> 
                    <div class="details">
                        <q>All the tears of the earth cannot carry a small boat of parents looking for their lost child</q>
                        <br> <br>
                        <cite>- Ghassan kanafani, return to haifa cover</cite>
                    </div>
            </div>

            <div class="card">
                <div class="imgBox">
                    <img src="img/2.jpg" alt="carlos ruiz zafon book">
                 </div> 
                    <div class="details">
                        <q>In the shop we buy and sell them, but in truth books have no owner. Every book you see here has been somebody’s best friend.</q>
                        <br> <br>
                        <cite>- Carlos Ruiz Zafón, The Shadow of the Wind</cite>
                    </div>
             </div>  

             <div class="card">
                <div class="imgBox">
                    <img src="img/4.jpg" alt="Susan abulhawa book">
                 </div> 
                    <div class="details">
                        <q>He was shocked by Death's lack of drama. of being realistic. From his quiet power.</q>
                        <br> <br>
                        <cite>- Susan Abulhawa, Mornings in Jenin</cite>
                    </div>
             </div>  
             
             <div class="card">
                <div class="imgBox">
                    <img src="img/8.jpg" alt="Stephen King book">
                 </div> 
                    <div class="details">
                        <q>On the day of my judgment, when I stand before God, and He asks me why did I kill one of his true miracles, what am I gonna say? That it was my job? My job?</q>
                        <br> <br>
                        <cite>- Stephen King, The Green Mile</cite>
                    </div>
             </div>

             <div class="card">
                <div class="imgBox">
                    <img src="img/3.jpg" alt="herman hesse book">
                </div>
                <div class="details">
                    <q> live in my dreams — that's what you sense. Other people live in dreams, but not in their own. That's the difference.</q>
                    <br> <br>
                    <cite>- Herman Hesse, Demian</cite>
                </div>
            </div>
        </div>
    </section>

    <!--footer-->
	<?php include 'includes/footer.php'?>

</body>
</html>