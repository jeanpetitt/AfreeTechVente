import React from 'react'
import "../styles/fruitList.css"

function FruitItem({name, cover, id, isBestSale}) {
  return (
    <li key={id} className='afre-fruit-item'>
        <img className='afre-fruit-item-cover' src={cover} alt={`${name} cover`} />
        {name}
        {isBestSale && <span>🔥</span>}
    </li>
  )
}

export default FruitItem