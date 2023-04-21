import { useState } from "react"
import "../styles/footer.css"

export const Footer = () => {
    const [inputValue, setInputValue] = useState('')

    function handleInput(e){
        setInputValue(e.target.value)
    }

    function handleBllur(){
        if (!inputValue.includes("@")){
            alert("ceci n'est pas une adresse email valide")
        }
    }

    return (
        <footer className="afre-footer">
            <div className="afre-footer-item">
                pour les passionnés des fruits 🌿🌱🌵
            </div>
            <div className="afre-footer-item">
                Laissez-nous votre email:
            </div>
            <input type="email"
                placeholder="Entrer-Votre Email"
                onChange={handleInput}
                value={inputValue}
                onBlur={handleBllur}    
            />
        </footer>
    )
}
