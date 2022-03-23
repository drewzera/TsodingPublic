let counterDisplayElem = document.querySelector('.counter-display');
let counterMinusElem = document.querySelector('.counter-down');
let counterPlusElem = document.querySelector('.counter-up');

let count=0;

updateDisplay();

function updateDisplay(){
    counterDisplayElem.innerHTML = count;
};

counterPlusElem.addEventListener("click",()=>{
    count++;
    updateDisplay();
});

counterMinusElem.addEventListener("click",()=>{
    count--;
    updateDisplay();
});