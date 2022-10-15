import React, { useState } from 'react';

import './Card.css';
import './Map.css';

import Building from './Building';

import mapBackground from '../assets/buildings/map_bottom.png';
import boydOrrImage from '../assets/buildings/boydOrr.png';
import libraryImage from '../assets/buildings/library.png';
import stAndrewsImage from '../assets/buildings/stAndrews.png';
import kelvinImage from '../assets/buildings/kelvin.png';
import josephBlackImage from '../assets/buildings/josephBlack.png';
import qmuImage from '../assets/buildings/qmu.png';
import alwynImage from '../assets/buildings/sirAlwyn.png';
import hiveImage from '../assets/buildings/hive.png';
import wolfsonImage from '../assets/buildings/wolfson.png';
import guuImage from '../assets/buildings/guu.png';
import mainImage from '../assets/buildings/main.png';
import adamSmithImage from '../assets/buildings/adamSmith.png';
import jwsImage from '../assets/buildings/jws.png';
import kelvingroveImage from '../assets/buildings/kelvingrove.png';

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
        "Library": libraryImage,
        "St Andrews": stAndrewsImage
    }

    // var intensity = {
    //     if intesity > 0.5 
    // }


    // Function to convert number of people to hex value

    // On state change, pass hex value to each child through props
    
    return (
        <div className="Card layout-map">
            <div className='Map'>
                <img src={mapBackground} className="map-image" ></img>
                <Building intensity={0.5} image={boydOrrImage}></Building>
                <Building intensity={0.5} image={libraryImage}></Building>
                <Building intensity={0.5} image={stAndrewsImage}></Building>
                <Building intensity={0.5} image={kelvinImage}></Building>
                <Building intensity={0.5} image={josephBlackImage}></Building>
                <Building intensity={0.5} image={qmuImage}></Building>
                <Building intensity={0.5} image={alwynImage}></Building>
                <Building intensity={0.5} image={hiveImage}></Building>
                <Building intensity={0.5} image={guuImage}></Building>
                <Building intensity={0.5} image={wolfsonImage}></Building>
                <Building intensity={0.5} image={mainImage}></Building>
                <Building intensity={0.5} image={adamSmithImage}></Building>
                <Building intensity={0.7} image={jwsImage}></Building>
                <Building intensity={0.1} image={kelvingroveImage}></Building>
            </div>
        </div>
    );
}

export default Map;