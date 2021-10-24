let arr = [0,1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f"];
let colorPicker1 = document.querySelector("#input-1");
let colorPicker2 = document.querySelector("#input-2");
let backgroundGradient = {
  background1 :"#",
  background2 : "#",
  generateRandomColors() {
  for(let i =0; i < 6 ; i++){
  let index1 = Math.floor(Math.random() * arr.length)
  let index2 = Math.floor(Math.random() * arr.length)
  this.background1+= arr[index1];
  this.background2+= arr[index2];
  this.gradientRendering()}
},
 gradientRendering () {
   let backgroundGradient = document.querySelector(".background-gradient");
backgroundGradient.style.backgroundImage = `linear-gradient(to right , ${this.background1} , ${this.background2})`;
document.querySelector(".value-1").innerHTML = this.background1;
document.querySelector(".value-2").innerHTML = this.background2;
document.querySelector(".color-1").style.backgroundColor = this.background1;
document.querySelector(".color-2").style.backgroundColor = this.background2;
 }

};
backgroundGradient.generateRandomColors();
let background2;
colorPicker2.addEventListener("input",function (){
  updateStop("background2",this.value);
});

colorPicker1.addEventListener("input",function (){
  updateStop("background1",this.value);
});

function updateStop(background,value){
  backgroundGradient[background] = value;
  backgroundGradient.gradientRendering(); 
}