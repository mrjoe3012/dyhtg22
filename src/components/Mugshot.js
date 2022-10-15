import './Mugshot.css'

import maleBody from '../assets/mugs/maleBody.png';
import maleHead from '../assets/mugs/maleHead.png';
import femaleBody from '../assets/mugs/femaleBody.png';
import femaleHead from '../assets/mugs/femaleHead.png';
import f1 from '../assets/mugs/femaleHair/1.png';
import f2 from '../assets/mugs/femaleHair/2.png';
import f3 from '../assets/mugs/femaleHair/3.png';
import m1 from '../assets/mugs/maleHair/1.png';
import m2 from '../assets/mugs/maleHair/2.png';
import m3 from '../assets/mugs/maleHair/3.png';

var maleHair = [m1, m2, m3]
var femaleHair = [f1, f2, f3]


function Mugshot(props)
{
    var body;
    var head;
    var hair = Math.floor(Math.random() * 3);

    if (props.person.sex == 'Male')
    {
        body = maleBody;
        head = maleHead
        hair = maleHair[hair]
    }
    else
    {
        body = femaleBody;
        head = femaleHead
        hair = femaleHair[hair]
    }

    return (
        <div className='Mug'>
            <img src={body} className='mug-component'></img>
            <img src={head} className='mug-component'></img>
            <img src={hair} className='mug-component'></img>
            <img src={hair} className='mug-component' style={{'filter': `opacity(0.3) drop-shadow(0 0 0 ${props.person.hair}) drop-shadow(0 0 0 ${props.person.hair}) drop-shadow(0 0 0 ${props.person.hair}) drop-shadow(0 0 0 ${props.person.hair})`}} ></img>
        </div>
    )
}

export default Mugshot;