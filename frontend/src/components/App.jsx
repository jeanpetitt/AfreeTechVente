import Banner from "./Banner"
import Cart from "./Cart"
import ShoppingList from "./ShoppingList";
import logo from '../assets/logo.png'

function App() {
  return(
    <div>
        <Banner>
            <img src={logo} alt="afreetech" className="img-afre" />
            <h1 className='afre-title'>AfreeTech Shop</h1>
        </Banner>
        <Cart/>
        <ShoppingList/>
    </div>
  );
}
export default App;
