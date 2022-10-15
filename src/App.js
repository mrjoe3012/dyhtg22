import './App.css';

import Nav from './components/Nav';
import Layout from './components/Layout';

function App() {
  return (
    <div className="App">
      <Nav className='app-nav'></Nav>
      <Layout className="app-layout"></Layout>
    </div>
  );
}

export default App;
