import './Layout.css'
import './Nav.css'
import logo from "../assets/other/title_logo.png"

function Nav()
{
    return (
        <div className="Nav layout-nav">
            {/* <h1>Guy Finder</h1> */}
            <img src = {logo} alt = "" className = "titleLogo" ></img>
        </div>
    )
}

export default Nav;