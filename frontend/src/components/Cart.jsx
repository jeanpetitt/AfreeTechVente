import React from 'react'
import "../styles/cart.css"


function Cart() {
    const manguePrice = 8
	const orangePrice = 10
	const tomatePrice = 15
  return (
    <div className='afree-cart'>
		<h2>Cart</h2>
		<ul>
			<li>mangue : {manguePrice}€</li>
			<li>orange : {orangePrice}€</li>
			<li>tomate : {tomatePrice}€</li>
		</ul>
		Total : {manguePrice + orangePrice + tomatePrice}€
	</div>
  )
}

export default Cart;
