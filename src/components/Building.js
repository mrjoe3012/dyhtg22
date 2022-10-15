import './Building.css'

function Building(props)
{
    return (
        <div className="Building">
            <h1>{props.name}</h1>
            <img src={props.image} className="building-image"></img>
        </div>
    )
}

export default Building;