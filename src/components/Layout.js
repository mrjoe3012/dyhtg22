import { useState } from 'react';

import Graph from './Graph'
import Map from "./Map";
import Person from "./Person";
import Options from './Options';

import './Layout.css'

function Layout()
{
    const [tab, setTab] = useState('map');

    const chooseTab = (tabName) => {
        setTab(tabName);
    }

    if (tab == 'map'){
        return (
            <div className="Layout">
                
                <Map></Map>
                <Person></Person>
                <Options onClick={chooseTab}></Options>
            </div>
        );
    }
    else if(tab == 'graph'){
        return (
            <div className="Layout">
                <Graph></Graph>
                <Person></Person>
                                <Options onClick={chooseTab}></Options>

            </div>
        );
    }


}

export default Layout;