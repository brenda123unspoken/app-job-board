// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;



import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import JobList from './components/JobList';
import PostJob from './components/PostJob';
import Login from './components/Login';

function App() {
  return (
    <Router>
      <div className="App">
        <h1>Job Board</h1>
        <Switch>
          <Route path="/jobs" component={JobList} />
          <Route path="/post-job" component={PostJob} />
          <Route path="/login" component={Login} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;

