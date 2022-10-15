import './Building.css'

function Building(props)
{
    return (
        <div className="Building">
            <img src={props.image} className="building-image" style={{'filter': `opacity(${props.intensity}) drop-shadow(0 0 0 red) drop-shadow(0 0 0 red)`}}></img>
        </div>
    )
}

export default Building;