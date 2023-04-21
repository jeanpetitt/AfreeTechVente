import React from 'react'
import { fruitList } from '../data/fruitList'

function ShoppingList() {
    const categories = fruitList.reduce(
		(acc, fruit) =>
			acc.includes(fruit.category) ? acc : acc.concat(fruit.category),
		[]
	)


  return (
    <div>
        <ul>
			{categories.map((cat) => (
					<li key={cat}>{cat}</li>
			))}
		</ul>
        <ul>
            {fruitList.map((fruit) => (
                <li key={fruit.id}>
                    {fruit.name}
                    {fruit.isBestSale && <span>🔥</span>}
                </li>
                // <p>{fruit.description}</p>
            ))}
        </ul>
    </div>
  )
}

export default ShoppingList