
import React from 'react'
import '../styles/banner.css'
import logo from '../assets/logo.png'

function Banner() {
    const title = "AfreeTech"
    return (
        <div className='title-afree'>
            <img src={logo} alt="afreetech" className="img-afre" />
            <h1>{title}</h1>
        </div>
    )
}

export default Banner;
