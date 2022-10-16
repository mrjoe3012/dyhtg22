import { useState } from 'react';

import './Card.css'
import './Layout.css'

function Graph() {

    const [graphImage, setGraphImage] = useState();

    function generateGraph() {
        setGraphImage("http://127.0.0.1:5000/get-interaction-graph?students=")
    }

    console.log(typeof(graphImage));

    return (
        <div className="Card layout-graph">
            <h1>Graph</h1>
            <button onClick={generateGraph}>Generate</button>
            <img src={graphImage}></img>
        </div>
    )
}

export default Graph;