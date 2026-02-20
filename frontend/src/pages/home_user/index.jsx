import React, {useState} from "react";


export default function HomeUser(){
    const token = localStorage.getItem('token')

    return(
        <div>
            <p>Essa é a página Home!!!</p>
            <p>Token: {token}</p>
        </div>
    )
}