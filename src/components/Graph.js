import { useState } from 'react';

import './Card.css'
import './Layout.css'
import './Graph.css'

function Graph() {

    const [graphImage, setGraphImage] = useState('');

    const [id, setId] = useState();

    function generateGraph(id) {
        setGraphImage(`http://127.0.0.1:5000/get-interaction-graph?students=${id}`)
    }

    const handleSubmit = (e) => {
        e.preventDefault();

        console.log(id);

        generateGraph(id);
        // setId('')
    }

    console.log(typeof(graphImage));

    return (
        <div className="Card layout-graph Graph">
            <form onSubmit={handleSubmit}>
                <input type="text" name="title" value={id} onChange={e => setId(e.target.value)}></input>
                <button type="submit" className="btn">Generate graph for students</button>
            </form>
            <img src={graphImage} className="graph-image"></img>
        </div>
    )
}

export default Graph;