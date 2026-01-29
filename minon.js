let cart = document.getElementById('cart-result');
cart.innerText = 0
cart.value=0
cart.innerHTML=cart.value

const kup1 = document.getElementById('kup1')
const kup2 = document.getElementById('kup2')
const kup3 = document.getElementById('kup3')
const kup4 = document.getElementById('kup4')
const kup5 = document.getElementById('kup5')
const reset = document.getElementById('reset')
const login = document.getElementById('login')
const login2 = document.getElementById('login1')
const yimg = document.getElementById('yimg')
const yprice = document.getElementById('yprice')
const yopis = document.getElementById('yopis')
const add1 = document.getElementById('add1')
const kup = document.getElementById('kup')
const dropcart = document.getElementById('dropcart')
const gragcart = document.getElementById('dragcart')

let minList =[
]

function cartfirst(){
    cart.value += 700
    cart.innerHTML=cart.value
}
function cartsecond(){
    cart.value += 1000
    cart.innerHTML=cart.value

}
function cartthird(){
    cart.value += 600
    cart.innerHTML=cart.value
}
function cartfourth(){
    cart.value += 100
    cart.innerHTML=cart.value
}
function cartfives(){
    cart.value += 200
    cart.innerHTML=cart.value
}
function res(){
    cart.value=0
    cart.innerHTML=cart.value
}
function login1(){
    login2.innerHTML='Welcome, '+ login.value
}
function cartadd(){
    cart.value += Number(yprice.value)
    cart.innerHTML=cart.value
}
function add(){
    add1.innerHTML=''
    if (yimg.value.slice(0, 8) == 'https://' || yimg.value.slice(0,11) == 'data:image/'  && yprice.value == Number(yprice.value)){
    console.log(add1)
    console.log(add1.innerHTML)
    console.log(minList)
    minList.push( {img:yimg.value, price:yprice.value, opis:yopis.value})
    minList.forEach((item, index) => {
        
        add1.innerHTML+=`
        <div class="card" id='${index}' draggable='true'>
        <div class="cart-kar4"><img class="cart-kar4" src=${item.img} alt=""></div>
        <div class="price">${item.price}$</div>
        <div class="opis4">${item.opis}</div>
        <button class="kup" id="dragcart" onclick="cartadd()">Add to cart</button>
        </div>
        `
        const Index = document.getElementById(index)
        Index.addEventListener('dragstart', (event) => {
            event.dataTransfer.setData('currentPrice', item.price)
        })
        dropcart.addEventListener('dragover', (event) => {
            event.preventDefault()
        })
        dropcart.addEventListener('drop', (event) => {
            event.preventDefault()
            const cardPrice = event.dataTransfer.getData('currentPrice')
            cart.value += Number(cardPrice)
            cart.innerHTML=cart.value
        })
    })
}
}
