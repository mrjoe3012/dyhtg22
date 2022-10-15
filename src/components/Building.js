import './Building.css'

function style_var(intensity, opacity)
{
    if(intensity < 0.1)
    {
        return {'filter': `opacity(${opacity}) drop-shadow(0 0 0 blue) drop-shadow(0 0 0 blue) drop-shadow(0 0 0 blue)`};
    } 
    else if(intensity < 0.2)
    {
        return {'filter': `opacity(${opacity}) drop-shadow(0 0 0 cyan) drop-shadow(0 0 0 cyan) drop-shadow(0 0 0 cyan)`};
    } 
    else if(intensity < 0.3)
    {
        return {'filter': `opacity(${opacity}) drop-shadow(0 0 0 green) drop-shadow(0 0 0 green) drop-shadow(0 0 0 green)`};
    } 
    else if(intensity < 0.4)
    {
        return {'filter': `opacity(${opacity}) drop-shadow(0 0 0 yellow) drop-shadow(0 0 0 yellow) drop-shadow(0 0 0 yellow)`};
    } 
    else if(intensity < 0.5)
    {
        return {'filter': `opacity(${opacity}) drop-shadow(0 0 0 orange) drop-shadow(0 0 0 orange) drop-shadow(0 0 0 orange)`};
    } 
    else {
        return {'filter' : `opacity(${opacity}) drop-shadow(0 0 0 red) drop-shadow(0 0 0 red) drop-shadow(0 0 0 red)`};
    }
}

function Building(props)
{
    var style_to_use = style_var(props.intensity, props.opacity)

    return (
        <div className="Building">
            <img src={props.image} className="building-image" style={style_to_use}></img>
        </div>
    )
}

export default Building;