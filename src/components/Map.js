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
    const buildings = {
        "Adam Smith Building": {
            'totalVisited': 44,
            'image': adamSmithImage
        },
        "Boyd Orr Building": {
            'totalVisited': 64,
            'image': boydOrrImage
        },
        "Glasgow University Union": {
            'totalVisited': 68,
            'image': guuImage
        },
        "James Watt Building": {
            'totalVisited': 36,
            'image': jwsImage
        },
        "Joseph Black Building": {
            'totalVisited': 16,
            'image': josephBlackImage
        },
        "Kelvin Building": {
            'totalVisited': 17,
            'image': kelvinImage
        },
        "Kelvingrove Park": {
            'totalVisited': 68,
            'image': kelvingroveImage
        },
        "Library": {
            'totalVisited': 66,
            'image': libraryImage
        },
        "Main Building": {
            'totalVisited': 85,
            'image': mainImage
        },
        "Queen Margaret Union": {
            'totalVisited': 68,
            'image': qmuImage
        },
        "Sir Alwyn Williams Building": {
            'totalVisited': 27,
            'image': alwynImage
        },
        "St Andrews Building": {
            'totalVisited': 42,
            'image': stAndrewsImage
        },
        "The Hive": {
            'totalVisited': 19,
            'image': hiveImage
        },
        "Wolfson Medical Building": {
            'totalVisited': 41,
            'image': wolfsonImage
        },
      }   

    var total = 0;

    for (const [key, value] of Object.entries(buildings)) {
        if (value.totalVisited > total)
        {
            total = value.totalVisited;
        }
    }

    // console.log(total)
    
    const [opacity, setOpacity] = useState(0.5);
    
    useEffect(() => {
        const interval = setInterval(() => {
            var x = 0.125; // Increase to increase range
            var y = 0.002; // Increase to speed up
            var offset = 0.5; // Increase to reduce transparency & increase sharpness

            var intensity_new = (Math.sin(Date.now() * y) * x) + offset;
            // console.log(intensity_new);
            setOpacity(intensity_new);
        }, 5);
      
        return () => clearInterval(interval);
      }, []);

    return (
        <div className="Card layout-map">
            <div className='Map'>
                <img src={mapBackground} className="map-image" ></img>
                <Building intensity={buildings['Boyd Orr Building'].totalVisited / total} opacity={opacity} image={boydOrrImage}></Building>
                <Building intensity={buildings['Library'].totalVisited / total} opacity={opacity}  image={libraryImage}></Building>
                <Building intensity={buildings['St Andrews Building'].totalVisited / total} opacity={opacity}  image={stAndrewsImage}></Building>
                <Building intensity={buildings['Kelvin Building'].totalVisited / total} opacity={opacity}  image={kelvinImage}></Building>
                <Building intensity={buildings['Joseph Black Building'].totalVisited / total} opacity={opacity}  image={josephBlackImage}></Building>
                <Building intensity={buildings['Queen Margaret Union'].totalVisited / total} opacity={opacity}  image={qmuImage}></Building>
                <Building intensity={buildings['Sir Alwyn Williams Building'].totalVisited / total} opacity={opacity}  image={alwynImage}></Building>
                <Building intensity={buildings['The Hive'].totalVisited / total} opacity={opacity}  image={hiveImage}></Building>
                <Building intensity={buildings['Glasgow University Union'].totalVisited / total} opacity={opacity}  image={guuImage}></Building>
                <Building intensity={buildings['Wolfson Medical Building'].totalVisited / total} opacity={opacity}  image={wolfsonImage}></Building>
                <Building intensity={buildings['Main Building'].totalVisited / total} opacity={opacity}  image={mainImage}></Building>
                <Building intensity={buildings['Adam Smith Building'].totalVisited / total} opacity={opacity}  image={adamSmithImage}></Building>
                <Building intensity={buildings['James Watt Building'].totalVisited / total} opacity={opacity}  image={jwsImage}></Building>
                <Building intensity={buildings['Kelvingrove Park'].totalVisited / total} opacity={opacity}  image={kelvingroveImage}></Building>
            </div>
            <div className='gradient-scale'>
                <p className='label'>Low</p>
                <img></img>
                <p className='gradient-scale'>High</p>
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