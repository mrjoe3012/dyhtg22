import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import './App.css';

import Nav from './components/Nav';
import Layout from './components/Layout';
import Login from './components/Login';
import React from 'react';

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/dashboard" element={
            <React.Fragment>
              <Nav className='app-nav'></Nav>
              <Layout className="app-layout"></Layout> 
            </React.Fragment>                
          } />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
