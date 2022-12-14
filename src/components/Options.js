import './Card.css'
import './Layout.css'
import './Options.css'

function Options(props)
{
    const onHeatmap = () => {
        props.onClick('map');
    }

    const onGraphs = () => {
        props.onClick('graph');
    }

    return (
        <div className="layout-options">
            {/* <div> */}
            <button onClick={onHeatmap} >Heatmap</button>
            <button onClick={onGraphs} >Graphs</button>
        </div>
    )
}

export default Options;