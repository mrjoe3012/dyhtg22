import Map from "./Map";
import Person from "./Person";
import GradientBar from "../assets/other/gradient.png"

import './Layout.css'

function Layout()
{
    return (
        <div className="Layout">
            <Map></Map>
            <Person></Person>
            <img src={GradientBar} alt ="" className="GradientBar"></img>
        </div>
    );
}

export default Layout;