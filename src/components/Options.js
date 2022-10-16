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
        <div className="layout-card layout-options">
            <button onClick={onHeatmap} className="heatmapButton">Heatmap</button>
            <button onClick={onGraphs} className="graphButton">Graphs</button>
        </div>
    )
}

export default Options;