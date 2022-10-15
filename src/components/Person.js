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
                <p><span className='header'>Name:</span> {person.name}</p>
                <p><span className='header'>Matriculation #:</span> {person.id}</p>
                <p><span className='header'>Age:</span> {person.age} years old</p>
                <p><span className='header'>Sex:</span> {person.sex}</p>
                <p><span className='header'>Academic year:</span> {person.year} Year</p>
                <p><span className='header'>Course:</span> {person.subject}</p>
                <p><span className='header'>Societies:</span> {person.societies}</p>
            </div>
        </div>
    );
}

export default Person;