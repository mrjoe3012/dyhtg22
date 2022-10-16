import { useState } from 'react';

import './Card.css'
import './Layout.css'
import './Graph.css'

function Graph() {

    const [graphImage, setGraphImage] = useState();

    const [id, setId] = useState('');
    const [strict, setStrict] = useState(false);

    function generateGraph(id) {
        setGraphImage(`http://127.0.0.1:5000/get-interaction-graph?students=${id}&strict=${strict}`)
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        generateGraph(id);
    }
    console.log(strict)
    return (
        <div className="Card layout-graph Graph">
            <form onSubmit={handleSubmit} className='filter'>
                <button type="submit" className="btn">Generate graph for students</button>
                <div>
                <label>Strict Search: </label>
                <input type="checkbox" value="strict" onChange={e => setStrict(e.target.value == "strict")}></input>
                </div>
                <input type="text" name="title" placeholder="Type student IDs here..." value={id} onChange={e => setId(e.target.value)}></input>
            </form>
            <img src={graphImage} className="graph-image"></img>
        </div>
    )
}

export default Graph;