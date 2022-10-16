import './Mugshot.css'

import maleBody from '../assets/mugs/_people_0007_male.png';
import femaleBody from '../assets/mugs/_people_0003_female.png';
import f1 from '../assets/mugs/femaleHair/_people_0000_femaleHair1.png';
import f2 from '../assets/mugs/femaleHair/_people_0001_femaleHair2.png';
import f3 from '../assets/mugs/femaleHair/_people_0002_femaleHair3.png';
import m1 from '../assets/mugs/maleHair/_people_0004_maleHair1.png';
import m2 from '../assets/mugs/maleHair/_people_0005_maleHair2.png';
import m3 from '../assets/mugs/maleHair/_people_0006_maleHair3.png';


import g1 from'../assets/buildingPhotos/_building_0008_kelvingrove.png';
import g2 from'../assets/buildingPhotos/_building_0009_jamesWatt.png';
import g3 from'../assets/buildingPhotos/_building_0010_adamSmith.png';
import g4 from'../assets/buildingPhotos/_building_0011_mainbuilding.png';
import g5 from'../assets/buildingPhotos/_building_0012_guu.png';
import g6 from'../assets/buildingPhotos/_building_0013_sirAl.png';
import g7 from'../assets/buildingPhotos/_building_0014_qmu.png';
import g8 from'../assets/buildingPhotos/_building_0015_SM-10-009.png';
import g9 from'../assets/buildingPhotos/_building_0016_kelvinbuilding.png';
import g10 from'../assets/buildingPhotos/_building_0017_standrews.png';
import g11 from'../assets/buildingPhotos/_building_0018_libraries.png';
import g12 from'../assets/buildingPhotos/_building_0019_wolfson.png';
import g13 from'../assets/buildingPhotos/_building_0020_hive.png';
import g14 from'../assets/buildingPhotos/_building_0021_boydOrr.png';

var buildingPhoto = [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14];
var maleHair = [m1, m2, m3]
var femaleHair = [f1, f2, f3]

function Mugshot(props)
{
    var rndBuild = Math.floor(Math.random() * 14);

    rndBuild = buildingPhoto[rndBuild]
    
    var body;
    var hair = Math.floor(Math.random() * 3);

    if (props.person.sex == 'Male')
    {
        body = maleBody;
        hair = maleHair[hair]
    }
    else
    {
        body = femaleBody;
        hair = femaleHair[hair]
    }

    return (
        <div className='Mug'>
            <img src={rndBuild} className='mug-component'></img>
            <img src={body} className='mug-component' alt=""></img>
            {/* <img src={head} className='mug-component'></img> */}
            <img src={hair} className='mug-component'></img>
            <img src={hair} className='mug-component' style={{'filter': `opacity(0.3) drop-shadow(0 0 0 ${props.person.hair}) drop-shadow(0 0 0 ${props.person.hair}) drop-shadow(0 0 0 ${props.person.hair}) drop-shadow(0 0 0 ${props.person.hair})`}} ></img>
        </div>
    )
}

export default Mugshot;