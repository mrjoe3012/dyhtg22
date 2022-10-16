import React, { useState, useEffect } from 'react';

import './Card.css';
import './Map.css';

import GradientBar from "../assets/other/gradient.png"

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
    const [opacity, setOpacity] = useState(0.5);
    
    useEffect(() => {
        const interval = setInterval(() => {
            var x = 0.1; // Increase to increase range
            var y = 0.002; // Increase to speed up
            var offset = 0.5; // Increase to reduce transparency & increase sharpness

            var intensity_new = (Math.sin(Date.now() * y) * x) + offset;
            // console.log(intensity_new);
            setOpacity(intensity_new);
        }, 5);
      
        return () => clearInterval(interval);
      }, []);

    // Function to convert number of people to hex value

    // On state change, pass hex value to each child through props
    
    return (
        <div className="Card layout-map">
            <div className='Map'>
                <img src={mapBackground} className="map-image" ></img>
                <Building intensity={0.4} opacity={opacity} image={boydOrrImage}></Building>
                <Building intensity={0.6} opacity={opacity}  image={libraryImage}></Building>
                <Building intensity={0.3} opacity={opacity}  image={stAndrewsImage}></Building>
                <Building intensity={0.05} opacity={opacity}  image={kelvinImage}></Building>
                <Building intensity={0.5} opacity={opacity}  image={josephBlackImage}></Building>
                <Building intensity={0.8} opacity={opacity}  image={qmuImage}></Building>
                <Building intensity={1} opacity={opacity}  image={alwynImage}></Building>
                <Building intensity={0.2} opacity={opacity}  image={hiveImage}></Building>
                <Building intensity={0.3} opacity={opacity}  image={guuImage}></Building>
                <Building intensity={0.5} opacity={opacity}  image={wolfsonImage}></Building>
                <Building intensity={0.4} opacity={opacity}  image={mainImage}></Building>
                <Building intensity={0.5} opacity={opacity}  image={adamSmithImage}></Building>
                <Building intensity={0.7} opacity={opacity}  image={jwsImage}></Building>
                <Building intensity={0.2} opacity={opacity}  image={kelvingroveImage}></Building>
            </div>
            <div className='heatmap-scale'>
                <p className='Low'>Low</p>
                
                    <img src={GradientBar} className="GradientBar"></img>
                    <p className='High'>High</p>
                {/* <p>High</p> */}
            </div>
        </div>
    );
}

export default Map;