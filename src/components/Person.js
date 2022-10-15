import './Card.css'
import './Person.css'

function Person()
{

    var person = {
        'id': '2627430',
        'name': 'Jamie Robb',
        'age': '19',
        'sex': 'Male',
        'year': '2nd',
        'subject': 'Computer Science',
        'height': '178',
        'hair': 'brown',
        'societies': 'UGRacing'
    }


    return (
        <div className="Card layout-person">
            <div>
                <img></img>
            </div>
            <div className='Person'>
                <p>{person.name}</p>
                <p>{person.id}</p>
                <p>{person.age} years old</p>
                <p>{person.sex}</p>
                <p>{person.year} Year</p>
                <p>{person.subject}</p>
            </div>
        </div>
    );
}

export default Person;