import Banner from "./Banner"
import Cart from "./Cart"
import { useState } from "react";
import ShoppingList from "./ShoppingList";
import logo from '../assets/logo.png'
import { Footer } from "./Footer";

function App() {
  const [cart, updateCart] = useState(0)
  return(
    <div>
        <Banner>
            <img src={logo} alt="afreetech" className="img-afre" />
            <h1 className='afre-title'>AfreeTech Shop</h1>
        </Banner>
        <Cart cart={cart} updateCart={updateCart}/>
        <ShoppingList cart={cart} updateCart={updateCart}/>
        <Footer/>
    </div>
  );
}
export default App;
