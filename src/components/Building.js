import './Building.css'

function style_var(int){
    intensity < ((100/163)/100)*30)? style_var(1) :  style_var(1);
    style_to_use = {{'filter': `opacity(${props.intensity}) drop-shadow(0 0 0 yellow) drop-shadow(0 0 0 yellow) drop-shadow(0 0 0 yellow)`}}
    intensity < ((100/163)/100)*60)? style_var(2) :  style_var(1);
    style_to_use = {{'filter': `opacity(${props.intensity}/2) drop-shadow(0 0 0 orange) drop-shadow(0 0 0 orange) drop-shadow(0 0 0 orange)`}}
    intensity > ((100/163)/100)*60)? style_var(3) :  style_var(1);
    style_to_use = {{'filter': `opacity(${props.intensity}/3) drop-shadow(0 0 0 red) drop-shadow(0 0 0 red) drop-shadow(0 0 0 red)`}}
    return style_to_use;
};

function Building(props)

{
    return (
        <div className="Building">
            <img src={props.image} className="building-image" style={style_to_use}></img>
            {/* <img src={props.image} className="building-image" style={{'filter': `opacity(${props.intensity}) drop-shadow(0 0 0 red) drop-shadow(0 0 0 red) drop-shadow(0 0 0 red)`}}></img> */}
        </div>
    )
}

export default Building;