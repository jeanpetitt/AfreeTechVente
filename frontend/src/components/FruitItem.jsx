import React from 'react'
import "../styles/fruitList.css"

const handleClick = (e) => {
  e.preventDefault();
	console.log("evenement:", e)

}


function FruitItem({name, cover, id, isBestSale}) {
  return (
    <li key={id} className='afre-fruit-item' onClick={handleClick}>
        <img className='afre-fruit-item-cover' src={cover} alt={`${name} cover`} />
        {name}
        {isBestSale && <span>🔥</span>}
    </li>
  )
}

export default FruitItem