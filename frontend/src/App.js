import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import CollectionList from './components/CollectionList';
import CollectionCreate from './components/CollectionCreate';
import CollectionSearch from './components/CollectionSearch';
import './styles/App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route exact path="/">
            <CollectionList />
          </Route>
          <Route path="/create">
            <CollectionCreate />
          </Route>
          <Route path="/search/:collectionId">
            <CollectionSearch />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;