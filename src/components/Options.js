import './Card.css'
import './Layout.css'

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
            <button onClick={onHeatmap} className="optionBtn">Heatmap</button>
            <button onClick={onGraphs} className="optionBtn">Graphs</button>
        </div>
    )
}

export default Options;