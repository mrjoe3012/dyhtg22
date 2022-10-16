import { Link } from 'react-router-dom';

import './Card.css'
import './Login.css'

import Logo from '../assets/uofg.png'

function Login() 
{
    return (
        <div className="Login">
            <img src={Logo} className='logo'></img>
            <div className="Card login-card">
                <h1>Guy Finder</h1>
                <form className='login-form'>
                    <input label="Username:"></input>
                    <input type="password" label="Password:"></input>
                    <Link to="/dashboard">
                        <button>Log In</button>
                    </Link>
                </form>
            </div>
        </div>
    )
}

export default Login;