import React, { useEffect, useState } from "react";
import axios from "axios";
import './styles.css'


export default function HomeUser() {
    const token = localStorage.getItem('token')
    const [usuarios, setUsuarios] = useState([])
    const [nome, setNome] = useState('')
    const [usuarioFiltro, setUsuarioFiltro] = useState([])


    const getUsuarios = async () => {
        try {
            const response = await axios.get(
                'http://127.0.0.1:8000/api/users/',
                {
                    headers: {Authorization: `Bearer ${token}`}
                }

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
        console.log(usuarios)
    }, [usuarios])

    const getUsuarioFiltro = async () => {
        try {
            const response = await axios.get(
                `http://127.0.0.1:8000/api/usuarios?nome=${nome}`,
                {
                    headers: {Authorization: `Bearer ${token}`}
                }
            )

            console.log("Filtro funcionou")
            setUsuarioFiltro(response.data)
        } catch (error) {
            console.log(error);

        }
    }

    function handleButton() {
        getUsuarioFiltro()
    }



    return (
        <div>
            <p>Essa é a página Home!!!</p>
            <div>
                <table border={1} className="tabela">
                <tr>
                    <th>Nome: </th>
                    <th>Email: </th>
                    <th>Telefone: </th>
                    <th>Tipo: </th>
                </tr>

                {usuarios.map((usuario, index) => (
                    <tr key={index}>
                        <td>{usuario.nome}</td>
                        <td>{usuario.email}</td>
                        <td>{usuario.telefone}</td>
                        <td>{usuario.tipo}</td>

                    </tr>
                ))}


            </table>
            </div>
            
            <div>
                <input
                    type="text"
                    value={nome}
                    onChange={(e) => setNome(e.target.value)}
                />
                <button onClick={handleButton}>Pesquisar</button>

                {usuarioFiltro.length != 0 ?
                    <table border={1} className="tabela">
                <tr>
                    <th>Nome: </th>
                    <th>Email: </th>
                    <th>Telefone: </th>
                    <th>Tipo: </th>
                </tr>

                {usuarioFiltro.map((usuario, index) => (
                    <tr key={index}>
                        <td>{usuario.nome}</td>
                        <td>{usuario.email}</td>
                        <td>{usuario.telefone}</td>
                        <td>{usuario.tipo}</td>

                    </tr>
                ))}


            </table>
                    : ""}
            </div>


        </div>
    )
}