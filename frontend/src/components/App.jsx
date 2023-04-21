import Banner from "./Banner"
import Cart from "./Cart"
import ShoppingList from "./ShoppingList";
import logo from '../assets/logo.png'
import { Footer } from "./Footer";

function App() {
  return(
    <div>
        <Banner>
            <img src={logo} alt="afreetech" className="img-afre" />
            <h1 className='afre-title'>AfreeTech Shop</h1>
        </Banner>
        <Cart/>
        <ShoppingList/>
        <Footer/>
    </div>
  );
}
export default App;
