import Map from "./Map";
import Person from "./Person";
import Info from "./Info";

import './Layout.css'

function Layout()
{
    return (
        <div className="Layout">
            <Map></Map>
            <Person></Person>
            <Info></Info>
        </div>
    );
}

export default Layout;