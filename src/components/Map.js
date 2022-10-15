import React, { useState } from 'react';

import './Card.css';
import './Map.css';

import Building from './Building';

import mapBackground from '../assets/buildings/map_bottom.png';
import boydOrrImage from '../assets/buildings/boydOrr.png';
import libraryImage from '../assets/buildings/library.png';

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
        "Boyd Orr": boydOrrImage,
        "Library": libraryImage
    }

    // Function to convert number of people to hex value

    // On state change, pass hex value to each child through props
    
    return (
        <div className="Card layout-map">
            <div className='Map'>
                <img src={mapBackground} className="map-image" ></img>
                <Building intensity={0.5} image={buildingImages["Boyd Orr"]}></Building>
                <Building intensity={0.5} image={buildingImages["Library"]}></Building>
            </div>
        </div>
    );
}

export default Map;