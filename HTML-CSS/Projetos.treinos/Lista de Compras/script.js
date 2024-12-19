let input = document.getElementById('item-input');
let button = document.getElementById('item-button');
let ul = document.getElementById('items');
let items = document.getElementsByTagName('li');
let itemButtons = document.getElementsByClassName("remove");


function criarelemento(){
    let li = document.createElement('li');
    
    let xButton = document.createElement('button');
    xButton.innerHTML = "X";
    xButton.className = "remove";
    
    li.appendChild(xButton);
    
    let text = document.createTextNode(input.value);
    
    li.appendChild(text);
    
    ul.appendChild(li);
    
    input.value = "";
    buttonEvents();
}

function deleteItem(){
    this.parentElement.remove();
}

function buttonEvents(){
    for(let i = 0; i < itemButtons.length(); i++){
        items[i].addEventListener("click", deleteItem);
    }
}

button.addEventListener('click', criarelemento)
buttonEvents();