import './Card.css'
import './Person.css'

import Mugshot from './Mugshot'

function Person()
{

    var person = {
        'id': '2627430',
        'name': 'Jamie Robb',
        'age': '19',
        'sex': 'Female',
        'year': '2nd',
        'subject': 'Computer Science',
        'height': '178',
        'hair': '#287456',
        'societies': 'UGRacing'
    }

    return (
        <div className="Card Person layout-person">
            <div className='Mugshot'>
                <Mugshot person={person}></Mugshot>
            </div>
            <div className='person-info'>
                <p>{person.name}</p>
                <p>{person.id}</p>
                <p>{person.age} years old</p>
                <p>{person.sex}</p>
                <p>{person.year} Year</p>
                <p>{person.subject}</p>
                <p>{person.societies}</p>
            </div>
        </div>
    );
}

export default Person;