import React from 'react'
import { fruitList } from '../data/fruitList'
import "../styles/shoppingList.css"
import FruitItem from './FruitItem'

function ShoppingList() {
    const categories = fruitList.reduce(
		(acc, fruit) =>
			acc.includes(fruit.category) ? acc : acc.concat(fruit.category),
		[]
	)


  return (
    <div className=''>
        <ul>
			{categories.map((cat) => (
				<li key={cat}>{cat}</li>
			))}
		</ul>
        <ul className='afre-fruit-list'>
            {fruitList.map((fruit) => (
                <FruitItem
					name={fruit.name}
					id={fruit.id}
					isBestSale={fruit.isBestSale}
					cover={fruit.image}
				/>
            ))}
        </ul>
    </div>
  )
}

export default ShoppingList