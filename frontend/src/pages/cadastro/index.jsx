import axios from "axios";
import { useEffect, useState } from "react";
import './styles.css'
import { useNavigate } from "react-router-dom";

export default function Cadastro() {
    const [mensagem, setMensagem] = useState()
    const [username, setUsername] = useState("")
    const [email, setEmail] = useState("")
    const [telefone, setTelefone] = useState("")
    const [password, setPassword] = useState("")
    const [tipo, setTipo] = useState("")

    const navigate = useNavigate()

    const criarUsuario = async () => {
        try{
            
            const response = await axios.post(
                "http://127.0.0.1:8000/api/register/",
                {
                    "username": username,
                    "email": email,
                    "telefone": telefone,
                    "password": password,
                    "tipo": tipo
                }
            )
            console.log(response.data)
    
            const resp = await axios.post(
                "http://127.0.0.1:8000/api/token/",
                {
                    username: username,
                    password: password
                }
    
            )
            localStorage.setItem('token', resp.data.access)
            navigate('/homeuser')
        } catch(error){
            console.log(error)
        }
        
    }


    return (
        <div className="container">
            <div className="inputContainer">
                <input type="text"
                    value={username}
                    placeholder="username"
                    onChange={(e) => setUsername(e.target.value)}
                />
                <input type="text"
                    value={email}
                    placeholder="email"
                    onChange={(e) => setEmail(e.target.value)}
                />
                <input type="text"
                    value={telefone}
                    placeholder="telefone"
                    onChange={(e) => setTelefone(e.target.value)}
                />
                <input type="password"
                    value={password}
                    placeholder="password"
                    onChange={(e) => setPassword(e.target.value)}
                />
                <input type="text"
                    value={tipo}
                    placeholder="tipo"
                    onChange={(e) => setTipo(e.target.value)}
                />

                <button onClick={criarUsuario}>Cadastrar</button>
            </div>
        </div>
    )
}