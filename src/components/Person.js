import React, { useState, useEffect } from 'react';


import './Card.css'
import './Person.css'

import Mugshot from './Mugshot'
import axios from 'axios'

var index = 0;

var defaultPerson = {};

function Person()
{
    const [people, setPeople] = useState('');
    const [person, setPerson] = useState(defaultPerson);

    useEffect(() => {
        // 👇️ only runs once
        axios.get('http://127.0.0.1:5000/get-people')
        .then(response => {
            setPeople(response.data);
            setPerson(response.data[Math.floor(Math.random() * response.data.length)]);
        },[]);//setPeople(response.data));
        // setPerson(people[0]);
        
      }, []); // 👈️ empty dependencies array

    useEffect(() => {
        const interval = setInterval(() => {
            if(people.length > 0)
            {
                index = Math.floor(Math.random() * people.length);
                setPerson(people[index]);
            }
        }, 10000);
      
        return () => clearInterval(interval);
      }, [people]);

    return (
        <div className="Card Person layout-person">
            <div className='Mugshot'>
                <Mugshot person={person}></Mugshot>
            </div>
            <div className='person-info'>
                <p><span className='header'>Name:</span> {person.name}</p>
                <p><span className='header'>Matriculation:</span> {person.id}</p>
                <p><span className='header'>Age:</span> {person.age}</p>
                <p><span className='header'>Sex:</span> {person.sex}</p>
                <p><span className='header'>Height:</span> {person.height}cm</p>
                <p><span className='header'>Academic year:</span> {person.year}</p>
                <p><span className='header'>Course:</span> {person.subject}</p>
                <p><span className='header'>Societies:</span> {person.societies}</p>
            </div>
        </div>
    );
}

export default Person;