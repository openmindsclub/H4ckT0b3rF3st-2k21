// declaration variable
let asideMenu = document.querySelectorAll("ul li");
let enterTaskToday = document.getElementById("task-today");
let enterTaskTommorow = document.getElementById("task-tommorow");
// let listTask = document.querySelectorAll(".today");
let content = document.querySelectorAll(".task-section");
let lengthTaskToBeComplete = document.querySelector(
  ".statistique .to-be-complet h2"
);
let lengthTaskComplete = document.querySelector(
  ".statistique .complet-task h2"
);
let startTimer = document.querySelector(".pomodoro .timer button");
var dataShow;
// Create Task
function createTask(idCheck, taskName, className) {
  // Create Div
  let divContainer = document.createElement("div");
  divContainer.classList.add("list-task");
  // Create checkBox and add Att
  let inputCheck = document.createElement("input");
  inputCheck.type = "checkbox";
  inputCheck.id = idCheck;
  inputCheck.classList.add("checkBox");
  // Create label and add Att
  let labelCheck = document.createElement("label");
  labelCheck.setAttribute("for", idCheck);
  labelCheck.classList.add("label");
  // Create icon and add Att
  let iconCheck = document.createElement("span");
  iconCheck.classList.add("material-icons-outlined");
  iconCheck.innerHTML = " done_all ";
  // Create Paregraph and add text
  let paragraph = document.createElement("p");
  paragraph.innerHTML = taskName;
  // Create close icon
  let iconClose = document.createElement("span");
  iconClose.classList.add("material-icons-outlined");
  iconClose.innerHTML = " close ";
  // Create icon-div
  let closeDiv = document.createElement("div");
  closeDiv.classList.add("close-div");
  // Append Ele
  labelCheck.appendChild(iconCheck);
  divContainer.appendChild(inputCheck);
  divContainer.appendChild(labelCheck);
  divContainer.appendChild(paragraph);
  closeDiv.appendChild(iconClose);
  divContainer.appendChild(closeDiv);
  // Add divContainer in Today Div
  document.querySelector(className).appendChild(divContainer);
}
function taskToBeComplete() {
  let t = document.querySelectorAll(".today .list-task");
  t = Array.from(t);

  return t.length;
}
function taskComplete() {
  let t = document.querySelectorAll(".complete .list-task");
  t = Array.from(t);

  return t.length;
}
document.body.onload = function () {
  lengthTaskToBeComplete.innerHTML = taskToBeComplete();
  lengthTaskComplete.innerHTML = taskComplete();
};
// add task today
enterTaskToday.addEventListener("keyup", (event) => {
  if (event.keyCode === 13) {
    createTask(enterTaskToday.value, enterTaskToday.value, ".today");
    lengthTaskToBeComplete.innerHTML = taskToBeComplete();
    enterTaskToday.value = "";
  }
});

// add task tommorow
enterTaskTommorow.addEventListener("keyup", (event) => {
  if (event.keyCode === 13) {
    createTask(enterTaskTommorow.value, enterTaskTommorow.value, ".tommorow");
    enterTaskTommorow.value = "";
  }
});

function showContent(data) {
  content.forEach((element) => {
    element.classList.remove("active");
  });
  document.querySelector(data).classList.add("active");
}
// change content when click menu
asideMenu.forEach((element) => {
  element.addEventListener("click", (e) => {
    dataShow = e.currentTarget.dataset.show;
    showContent(dataShow);
  });
});
// multiple id check in html

// check complete task and remove task
content.forEach((element) => {
  element.addEventListener("click", (e) => {
    if (e.target.innerHTML == " close ") {
      e.target.parentElement.parentElement.remove();
    }
    if (e.target.innerHTML == " done_all ") {
      // e.target.parentElement.parentElement.remove();
      let cloneDiv = e.target.parentElement.parentElement.cloneNode(true);
      document.querySelector(".complete").appendChild(cloneDiv);
      e.target.parentElement.parentElement.remove();
      lengthTaskComplete.innerHTML = taskComplete();
    }
    if (element.classList.contains("today")) {
      if (
        e.target.innerHTML == " close " ||
        e.target.innerHTML == " done_all "
      ) {
        lengthTaskToBeComplete.innerHTML = taskToBeComplete();
      }
    }
    if (element.classList.contains("complete")) {
      if (
        e.target.innerHTML == " close " ||
        e.target.innerHTML == " done_all "
      ) {
        lengthTaskComplete.innerHTML = taskComplete();
      }
    }
  });
});
// Pomodoro Timer
startTimer.onclick = function () {
  startTimer.previousElementSibling.firstElementChild.innerHTML = "24";
  let minute = parseInt(
    startTimer.previousElementSibling.firstElementChild.innerHTML
  );
  startTimer.previousElementSibling.lastElementChild.innerHTML = "59";
  let second = parseInt(
    startTimer.previousElementSibling.lastElementChild.innerHTML
  );
  let secondTime = setInterval(() => {
    second--;
    startTimer.previousElementSibling.lastElementChild.innerHTML = second;
    if (
      second == "9" ||
      second == "8" ||
      second == "7" ||
      second == "6" ||
      second == "5" ||
      second == "4" ||
      second == "3" ||
      second == "2" ||
      second == "1" ||
      second == "0"
    ) {
      startTimer.previousElementSibling.lastElementChild.innerHTML = `0${second}`;
    }
    if (second === 0) {
      if (minute === 0) {
        clearInterval(secondTime);
      }
      second = 60;
    }
  }, 1000);
  let minuteTime = setInterval(() => {
    minute--;
    startTimer.previousElementSibling.firstElementChild.innerHTML = minute;
    if (
      minute == "9" ||
      minute == "8" ||
      minute == "7" ||
      minute == "6" ||
      minute == "5" ||
      minute == "4" ||
      minute == "3" ||
      minute == "2" ||
      minute == "1" ||
      minute == "0"
    ) {
      startTimer.previousElementSibling.firstElementChild.innerHTML = `0${minute}`;
    }
    if (minute === 0) {
      clearInterval(minuteTime);
    }
  }, 60000);

};
