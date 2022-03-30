let counterDisplayElem = document.querySelector('.counter-display');
let counterMinusElem = document.querySelector('.counter-down');
let counterPlusElem = document.querySelector('.counter-up');
let newCounter = document.querySelector('.new-counter');
const para = document.createElement('tr');

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

function addRow() {
    var i = 2 
    var tbody = document.getElementById('addRef').insertRow(i);
    cell0 = tbody.insertCell(0);
    cell1 = tbody.insertCell(1);
    cell2 = tbody.insertCell(2);
    cell3 = tbody.insertCell(3);
    cell4 = tbody.insertCell(4);
    cell5 = tbody.insertCell(5);
    cell0.innerHTML= "Enter Item Name Here";
    cell1.innerHTML = "Explaination";
    cell2.innerHTML = "";
    cell3.innerHTML = "";
    cell4.innerHTML = "";
    cell5.innerHTML = "";
    i=i+1;
}