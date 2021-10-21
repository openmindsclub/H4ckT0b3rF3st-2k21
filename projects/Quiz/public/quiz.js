let count = 0;
document.getElementById("link").addEventListener("click", () => {
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    var generator = timeout();
    window.a = setInterval(() => {
        document.getElementById("time").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time").innerText = "00" + ":" + "00";
            document.getElementById("box1").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(window.a);
        }
    }, 2000);
})
function starttimer() {
    clearInterval(window.a)
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    let a = document.getElementById("time")
    a.setAttribute("id", "changedtime");
    document.getElementById("changedtime").innerText = "00" + ":" + "00";
    let wrongans = document.getElementById("no");
    wrongans.pause()
    var generator = timeout();
    window.b = setInterval(() => {
        document.getElementById("time2").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time2").innerText = "00" + ":" + "00";
            document.getElementById("box2").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(window.b);
        }
    }, 2000);
}
function starttimer2() {
    clearInterval(window.b)
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    let b = document.getElementById("time2")
    b.setAttribute("id", "changedtime2");
    document.getElementById("changedtime2").innerText = "00" + ":" + "00";
    let wrongans = document.getElementById("no");
    wrongans.pause()
    var generator = timeout();
    window.c = setInterval(() => {
        document.getElementById("time3").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time3").innerText = "00" + ":" + "00";
            document.getElementById("box3").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(window.c);
        }
    }, 2000);
}
function starttimer3() {
    clearInterval(window.c);
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    let c = document.getElementById("time3")
    c.setAttribute("id", "changedtime3");
    document.getElementById("changedtime3").innerText = "00" + ":" + "00";
    let wrongans = document.getElementById("no");
    wrongans.pause()
    var generator = timeout();
    window.d = setInterval(() => {
        document.getElementById("time4").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time4").innerText = "00" + ":" + "00";
            document.getElementById("box4").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(window.d);
        }
    }, 2000);
}
function starttimer4() {
    clearInterval(window.d);
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    let d = document.getElementById("time4")
    d.setAttribute("id", "changedtime4");
    document.getElementById("changedtime4").innerText = "00" + ":" + "00";
    let wrongans = document.getElementById("no");
    wrongans.pause()
    var generator = timeout();
    window.e = setInterval(() => {
        document.getElementById("time5").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time5").innerText = "00" + ":" + "00";
            document.getElementById("box5").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(window.e);
        }
    }, 2000);
}
function starttimer5() {
    clearInterval(window.e);
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    let e = document.getElementById("time5")
    e.setAttribute("id", "changedtime5");
    document.getElementById("changedtime5").innerText = "00" + ":" + "00";
    let wrongans = document.getElementById("no");
    wrongans.pause()
    var generator = timeout();
    window.problem = setInterval(() => {
        document.getElementById("problem").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("problem").innerText = "00" + ":" + "00";
            document.getElementById("box6").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(window.problem);
        }
    }, 2000);
}
function starttimer6() {
    console.log(window.problem)
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    let z = document.getElementById("problem")
    z.setAttribute("id", "changedtime6");
    document.getElementById("changedtime6").innerText = "00" + ":" + "00";
    let wrongans = document.getElementById("no");
    wrongans.pause()
    var generator = timeout();
    window.interval = setInterval(() => {
        document.getElementById("time7").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time7").innerText = "00" + ":" + "00";
            document.getElementById("box7").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(window.interval);
        }
    }, 2000);
}
function starttimer7() {
    clearInterval(window.interval);
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    let g = document.getElementById("time7")
    g.setAttribute("id", "changedtime7");
    document.getElementById("changedtime7").innerText = "00" + ":" + "00";
    let wrongans = document.getElementById("no");
    wrongans.pause()
    var generator = timeout();
    window.h = setInterval(() => {
        document.getElementById("time8").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time8").innerText = "00" + ":" + "00";
            document.getElementById("box8").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(window.h);
        }
    }, 2000);
}
function starttimer8() {
    clearInterval(window.h);
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    let h = document.getElementById("time8")
    h.setAttribute("id", "changedtime8");
    document.getElementById("changedtime8").innerText = "00" + ":" + "00";
    let wrongans = document.getElementById("no");
    wrongans.pause()
    var generator = timeout();
    window.i = setInterval(() => {
        document.getElementById("time9").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time9").innerText = "00" + ":" + "00";
            document.getElementById("box9").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(window.i);
        }
    }, 2000);
}
function starttimer9() {
    clearInterval(window.i);
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    let i = document.getElementById("time9")
    i.setAttribute("id", "changedtime9");
    document.getElementById("changedtime9").innerText = "00" + ":" + "00";
    let wrongans = document.getElementById("no");
    wrongans.pause()
    var generator = timeout();
    window.j = setInterval(() => {
        document.getElementById("time10").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time10").innerText = "00" + ":" + "00";
            document.getElementById("box10").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(window.j);
        }
    }, 2000);
}
function starttimer10() {
    clearInterval(window.j);
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    let j = document.getElementById("time10")
    j.setAttribute("id", "changedtime10");
    document.getElementById("changedtime10").innerText = "00" + ":" + "00";
    let wrongans = document.getElementById("no");
    wrongans.pause()
    var generator = timeout();
    window.k = setInterval(() => {
        document.getElementById("time11").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time11").innerText = "00" + ":" + "00";
            document.getElementById("box11").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(window.k);
        }
    }, 2000);
}
function starttimer11() {
    clearInterval(window.k);
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    let k = document.getElementById("time11")
    k.setAttribute("id", "changedtime11");
    document.getElementById("changedtime11").innerText = "00" + ":" + "00";
    let wrongans = document.getElementById("no");
    wrongans.pause()
    var generator = timeout();
    window.m = setInterval(() => {
        document.getElementById("time12").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time12").innerText = "00" + ":" + "00";
            document.getElementById("box12").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(window.m);
        }
    }, 2000);
}
function starttimer12() {
    clearInterval(window.m);
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    let l = document.getElementById("time12")
    l.setAttribute("id", "changedtime12");
    document.getElementById("changedtime12").innerText = "00" + ":" + "00";
    let wrongans = document.getElementById("no");
    wrongans.pause()
    var generator = timeout();
    window.n = setInterval(() => {
        document.getElementById("time13").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time13").innerText = "00" + ":" + "00";
            document.getElementById("box13").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(window.n);
        }
    }, 2000);
}
function starttimer13() {
    clearInterval(window.n);
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    let m = document.getElementById("time13")
    m.setAttribute("id", "changedtime13");
    document.getElementById("changedtime13").innerText = "00" + ":" + "00";
    let wrongans = document.getElementById("no");
    wrongans.pause()
    var generator = timeout();
    window.l = setInterval(() => {
        document.getElementById("time14").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time14").innerText = "00" + ":" + "00";
            document.getElementById("box14").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(window.l);
        }
    }, 2000);
}
function starttimer14() {
    clearInterval(window.l);
    function* timeout() {
        var value = 60
        while (value > 0) {
            yield value--;
        }
    }
    let m = document.getElementById("time14")
    m.setAttribute("id", "changedtime14");
    document.getElementById("changedtime14").innerText = "00" + ":" + "00";
    let wrongans = document.getElementById("no");
    wrongans.pause()
    var generator = timeout();
    window.o = setInterval(() => {
        document.getElementById("time15").innerText = "00" + ":" + generator.next().value;
        if (generator.next().value == undefined) {
            document.getElementById("time15").innerText = "00" + ":" + "00";
            document.getElementById("box15").innerHTML = `<h5 style="color:rgba(24, 45, 236, 0.897);">Time Up</h5>`
            let wrongans = document.getElementById("no");
            wrongans.play()
            clearInterval(window.o);
        }
    }, 2000);
}
function starttimer15() {
    clearInterval(window.o);
    document.getElementById("time15").innerText = "00" + ":" + "00";
}
document.getElementById("ans1").addEventListener("click",function() {
    let otherbtns = document.getElementsByClassName("otheroption1");
    for (const btns of otherbtns) {
        btns.setAttribute("disabled", "true");
    }
    clearInterval(window.a);
    let ans = document.getElementById("ans1").value
    document.getElementById("box1").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans1").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
}, { once: true })
document.getElementById("ans2").addEventListener("click",function () {
    let otherbtns1 = document.getElementsByClassName("otheroption2");
    for (const btns of otherbtns1) {
        btns.setAttribute("disabled", "true");
    }
    clearInterval(window.b);
    let ans = document.getElementById("ans2").value
    document.getElementById("box2").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans2").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
},{ once: true })
document.getElementById("ans3").addEventListener("click",function () {
    let otherbtns2 = document.getElementsByClassName("otheroption3");
    for (const btns of otherbtns2) {
        btns.setAttribute("disabled", "true");
    }
    clearInterval(window.c);
    let ans = document.getElementById("ans3").value
    document.getElementById("box3").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans3").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
},{ once: true })
document.getElementById("ans4").addEventListener("click",function () {
    let otherbtns3 = document.getElementsByClassName("otheroption4");
    for (const btns of otherbtns3) {
        btns.setAttribute("disabled", "true");
    }
    clearInterval(window.d);
    let ans = document.getElementById("ans4").value
    document.getElementById("box4").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans4").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
},{ once: true })
document.getElementById("ans5").addEventListener("click",function () {
    let otherbtns4 = document.getElementsByClassName("otheroption5");
    for (const btns of otherbtns4) {
        btns.setAttribute("disabled", "true");
    }
    clearInterval(window.e);
    let ans = document.getElementById("ans5").value
    document.getElementById("box5").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans5").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
},{ once: true })
document.getElementById("ans6").addEventListener("click",function () {
    let otherbtns5 = document.getElementsByClassName("otheroption6");
    for (const btns of otherbtns5) {
        btns.setAttribute("disabled", "true");
    }
    clearInterval(window.problem);
    let ans = document.getElementById("ans6").value
    document.getElementById("box6").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans6").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
},{ once: true })
document.getElementById("ans7").addEventListener("click",function () {
    let otherbtns6 = document.getElementsByClassName("otheroption7");
    for (const btns of otherbtns6) {
        btns.setAttribute("disabled", "true");
    }
    clearInterval(window.interval);
    let ans = document.getElementById("ans7").value
    document.getElementById("box7").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans7").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
},{ once: true })
document.getElementById("ans8").addEventListener("click",function () {
    let otherbtns7 = document.getElementsByClassName("otheroption8");
    for (const btns of otherbtns7) {
        btns.setAttribute("disabled", "true");
    }
    clearInterval(window.h);
    let ans = document.getElementById("ans8").value
    document.getElementById("box8").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans8").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
},{ once: true })
document.getElementById("ans9").addEventListener("click",function () {
    let otherbtns8 = document.getElementsByClassName("otheroption9");
    for (const btns of otherbtns8) {
        btns.setAttribute("disabled", "true");
    }
    clearInterval(window.i);
    let ans = document.getElementById("ans9").value
    document.getElementById("box9").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans9").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
},{ once: true })
document.getElementById("ans10").addEventListener("click",function () {
    let otherbtns9 = document.getElementsByClassName("otheroption10");
    for (const btns of otherbtns9) {
        btns.setAttribute("disabled", "true");
    }
    clearInterval(window.j);
    let ans = document.getElementById("ans10").value
    document.getElementById("box10").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans10").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
},{ once: true })
document.getElementById("ans11").addEventListener("click",function () {
    let otherbtns10 = document.getElementsByClassName("otheroption11");
    for (const btns of otherbtns10) {
        btns.setAttribute("disabled", "true");
    }
    clearInterval(window.k);
    let ans = document.getElementById("ans11").value
    document.getElementById("box11").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans11").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
},{ once: true })
document.getElementById("ans12").addEventListener("click",function () {
    let otherbtns11 = document.getElementsByClassName("otheroption12");
    for (const btns of otherbtns11) {
        btns.setAttribute("disabled", "true");
    }
    clearInterval(window.m);
    let ans = document.getElementById("ans12").value
    document.getElementById("box12").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans12").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
},{ once: true })
document.getElementById("ans13").addEventListener("click",function () {
    let otherbtns12 = document.getElementsByClassName("otheroption13");
    for (const btns of otherbtns12) {
        btns.setAttribute("disabled", "true");
    }
    clearInterval(window.n);
    let ans = document.getElementById("ans13").value
    document.getElementById("box13").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans13").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
},{ once: true })
document.getElementById("ans14").addEventListener("click",function () {
    let otherbtns13 = document.getElementsByClassName("otheroption14");
    for (const btns of otherbtns13) {
        btns.setAttribute("disabled", "true");
    }
    clearInterval(window.l);
    let ans = document.getElementById("ans14").value
    document.getElementById("box14").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans14").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
},{ once: true })
document.getElementById("ans15").addEventListener("click",function () {
    let otherbtns14 = document.getElementsByClassName("otheroption15");
    for (const btns of otherbtns14) {
        btns.setAttribute("disabled", "true");
    }
    clearInterval(window.o);
    let ans = document.getElementById("ans15").value
    document.getElementById("box15").innerHTML = `<p><strong>Correct Ans : </strong>${ans}</p>`
    document.getElementById("ans15").style.backgroundColor = "rgba(54, 128, 76, 0.833)"
    let music = document.getElementById("yes");
    music.play()
    count++
},{ once: true })
console.log(count);
let wrongbtns = document.getElementsByClassName("wrong");
console.log(wrongbtns, typeof wrongbtns)
for (const btns of wrongbtns) {
    btns.addEventListener("click",function () {
            console.log("Button clicked!");
            btns.style.backgroundColor = "rgba(255, 2, 2, 0.877)"
            let wrongans = document.getElementById("no");
            wrongans.play();
        },
        { once: true }
    );

    /* btns.style.backgroundColor = "rgba(255, 2, 2, 0.877)"
     let wrongans = document.getElementById("no");
     wrongans.play();*/

}
function displayscore() {
    let name = document.getElementById("inpt").value
    document.getElementById("innerbox").innerHTML = `Thank you ${name} Your Score: <strong>${count}</strong>`
}