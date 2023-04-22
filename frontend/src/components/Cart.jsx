import React, {useState} from 'react'
import "../styles/cart.css"


function Cart({cart, updateCart}) {
	const manguePrice = 8
	const [isOPen, setIsOpen] = useState(false)
  return isOPen ? (
    <div className='afre-cart'>
		<button onClick={() => setIsOpen(false)} className='.afre-cart-add-button'>Fermer</button>
		<h2>Cart</h2>
		
		Total : {manguePrice *cart}€
		<button onClick={() => updateCart(0)} className='.afre-cart-add-button'>vider le panier</button>
	</div>
	
  ): 
  <div className="afre-cart-closed">
	<button onClick={() => setIsOpen(true)}>ouvrir le panier</button>
  </div>
}

export default Cart;
