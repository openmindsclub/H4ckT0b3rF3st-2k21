let count = 0;
document.getElementById("link").addEventListener("click", () => {
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    var generator = timeout();
    let a = setInterval(() => {
        document.getElementById("time").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time").innerText = "00" + ":" + "00";
            document.getElementById("box1").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(a);
        }
    }, 2000);
})
function starttimer() {
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    var generator = timeout();
    let b = setInterval(() => {
        document.getElementById("time2").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time2").innerText = "00" + ":" + "00";
            document.getElementById("box2").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(b);
        }
    }, 2000);
}
function starttimer2() {
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    var generator = timeout();
    let c = setInterval(() => {
        document.getElementById("time3").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time3").innerText = "00" + ":" + "00";
            document.getElementById("box3").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(c);
        }
    }, 2000);
}
function starttimer3() {
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    var generator = timeout();
    let d = setInterval(() => {
        document.getElementById("time4").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time4").innerText = "00" + ":" + "00";
            document.getElementById("box4").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(d);
        }
    }, 2000);
}
function starttimer4() {
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    var generator = timeout();
    let e = setInterval(() => {
        document.getElementById("time5").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time5").innerText = "00" + ":" + "00";
            document.getElementById("box5").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(e);
        }
    }, 2000);
}
function starttimer5() {
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    var generator = timeout();
    let f = setInterval(() => {
        document.getElementById("time6").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time6").innerText = "00" + ":" + "00";
            document.getElementById("box6").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(f);
        }
    }, 2000);
}
function starttimer6() {
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    var generator = timeout();
    let g = setInterval(() => {
        document.getElementById("time7").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time7").innerText = "00" + ":" + "00";
            document.getElementById("box7").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(g);
        }
    }, 2000);
}
function starttimer7() {
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    var generator = timeout();
    let h = setInterval(() => {
        document.getElementById("time8").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time8").innerText = "00" + ":" + "00";
            document.getElementById("box8").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(h);
        }
    }, 2000);
}
function starttimer8() {
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    var generator = timeout();
    let i = setInterval(() => {
        document.getElementById("time9").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time9").innerText = "00" + ":" + "00";
            document.getElementById("box9").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(i);
        }
    }, 2000);
}
function starttimer9() {
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    var generator = timeout();
    let i = setInterval(() => {
        document.getElementById("time10").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time10").innerText = "00" + ":" + "00";
            document.getElementById("box10").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(i);
        }
    }, 2000);
}
function starttimer10() {
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    var generator = timeout();
    let j = setInterval(() => {
        document.getElementById("time11").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time11").innerText = "00" + ":" + "00";
            document.getElementById("box11").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(j);
        }
    }, 2000);
}
function starttimer11() {
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    var generator = timeout();
    let k = setInterval(() => {
        document.getElementById("time12").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time12").innerText = "00" + ":" + "00";
            document.getElementById("box12").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(k);
        }
    }, 2000);
}
function starttimer12() {
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    var generator = timeout();
    let l = setInterval(() => {
        document.getElementById("time13").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time13").innerText = "00" + ":" + "00";
            document.getElementById("box13").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(l);
        }
    }, 2000);
}
function starttimer13() {
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    var generator = timeout();
    let m = setInterval(() => {
        document.getElementById("time14").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time14").innerText = "00" + ":" + "00";
            document.getElementById("box14").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(m);
        }
    }, 2000);
}
function starttimer14() {
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    var generator = timeout();
    let n = setInterval(() => {
        document.getElementById("time15").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time15").innerText = "00" + ":" + "00";
            document.getElementById("box15").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(n);
        }
    }, 2000);
}
function showans() {
    let ans = document.getElementById("ans1").value
    document.getElementById("box1").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans1").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
}
function showanstwo() {
    let ans = document.getElementById("ans2").value
    document.getElementById("box2").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans2").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
}
function showansthree() {
    let ans = document.getElementById("ans3").value
    document.getElementById("box3").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans3").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
}
function showansfour() {
    let ans = document.getElementById("ans4").value
    document.getElementById("box4").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans4").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
}
function showansfive() {
    let ans = document.getElementById("ans5").value
    document.getElementById("box5").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans5").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
}
function showanssix() {
    let ans = document.getElementById("ans6").value
    document.getElementById("box6").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans6").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
}
function showansseven() {
    let ans = document.getElementById("ans7").value
    document.getElementById("box7").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans7").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
}
function showanseight() {
    let ans = document.getElementById("ans8").value
    document.getElementById("box8").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans8").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
}
function showansnine() {
    let ans = document.getElementById("ans9").value
    document.getElementById("box9").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans9").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
}
function showansten() {
    let ans = document.getElementById("ans10").value
    document.getElementById("box10").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans10").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
}
function showanseleven() {
    let ans = document.getElementById("ans11").value
    document.getElementById("box11").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans11").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
}
function showans12() {
    let ans = document.getElementById("ans12").value
    document.getElementById("box12").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans12").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
}
function showansthirteen() {
    let ans = document.getElementById("ans13").value
    document.getElementById("box13").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans13").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
}
function showans14() {
    let ans = document.getElementById("ans14").value
    document.getElementById("box14").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans14").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
}
function showans15() {
    let ans = document.getElementById("ans15").value
    document.getElementById("box15").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans15").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
}
console.log(count);
let wrongbtns = document.getElementsByClassName("wrong");
console.log(wrongbtns, typeof wrongbtns)
for (const btns of wrongbtns) {
    btns.addEventListener("click", () => {
        btns.style.backgroundColor = "rgba(255, 2, 2, 0.877)"
        let wrongans = document.getElementById("no");
        wrongans.play()

    })
}
function displayscore() {
   let name=document.getElementById("inpt").value
    document.getElementById("innerbox").innerHTML=`Thank you ${name} Your Score: <p>${count}<>`
}