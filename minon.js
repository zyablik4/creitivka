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
