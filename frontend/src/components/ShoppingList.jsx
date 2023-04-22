import React from 'react'
import { fruitList } from '../data/fruitList'
import "../styles/shoppingList.css"
import FruitItem from './FruitItem'

function ShoppingList({ cart, updateCart }) {
    const categories = fruitList.reduce(
		(acc, fruit) =>
			acc.includes(fruit.category) ? acc : acc.concat(fruit.category),
		[]
	)


  return (
    <div className='afre-shoppingList'>
        {/* <ul>
			{categories.map((cat) => (
				<li key={cat}>{cat}</li>
			))}
		</ul> */}
        <ul className='afre-fruit-list'>
            {fruitList.map(({name,id, image, isBestSale}) => (
				<div id={id}>
					<FruitItem
						name={name}
						id={id}
						isBestSale={isBestSale}
						cover={image}
					/>
					<button onClick={() => updateCart(cart + 1)}>Ajouter</button>
				</div>
            ))}
        </ul>
    </div>
  )
}

export default ShoppingList