import React, { useEffect, useState } from "react";
import axios from "axios";


export default function HomeUser() {
    const token = localStorage.getItem('token')
    const [usuarios, setUsuarios] = useState([])

    const getUsuarios = async () => {
        try {
            const response = await axios.get(
                'http://127.0.0.1:8000/api/usuarios'

            )

            console.log("Deu certo");
            setUsuarios(response.data)

        } catch (error) {
            console.log(error);

        }
    }

    useEffect(() => {
        getUsuarios()
    }, [])

    useEffect(() => {
        console.log(usuarios[0])
    }, [usuarios])



    return (
        <div>
            <p>Essa é a página Home!!!</p>
            <table border={1}>
                <tr>
                    <th>Nome: </th>
                    <th>Email: </th>
                </tr>

                {usuarios.map((usuario, index) => (
                    <tr key={index}>
                        <td>{usuario.nome}</td>
                        <td>{usuario.email}</td>

                    </tr>
                ))}


            </table>

        </div>
    )
}