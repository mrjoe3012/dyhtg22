import React, { useState } from 'react';

import './Card.css';
import './Map.css';

import Building from './Building';

import mapBackground from '../assets/buildings/map_placeholder.jpg';
import boydOrrImage from '../assets/buildings/boyd-orr.jpg';

function Map()
{
    // const [time, setTime] = 

    // Data structure containing number of people in each building for each time
    var buildingLogs = {
        "0000": {
            "Boyd Orr": 20,
            "The Hive": 34
        },
        "0100": {
            "Boyd Orr": 7,
            "The Hive": 22
        }    
    }

    var buildingImages = {
        "Boyd Orr": boydOrrImage
    }

    // Function to convert number of people to hex value

    // On state change, pass hex value to each child through props
    
    return (
        <div className="Card layout-map">
            <div className='Map'>
                <h1>Map</h1>
                <img src={mapBackground} className="map-image"></img>
                {/* <Building name="Boyd Orr" image={buildingImages["Boyd Orr"]}></Building> */}
                <Building name="The Hive"></Building>
            </div>
        </div>
    );
}

export default Map;