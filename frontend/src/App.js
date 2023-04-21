import React, { Component } from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import FruitList from "./component/FruitView";
import FruitDetail from "./component/FruitDetails";
import FruitPost from "./component/FruitPost";
import Header from "./component/Header";


class App extends Component {
  render() {
    return (
      <div className='App'>
        <Header/>
        <Router>
          <Switch>
            <Route path='/' exact component={FruitList} />
            <Route path='/fruits/:fruitId/' component={FruitDetail} />
            <Route path='/fruits/add' component={FruitPost} />
            <Route>404 Not Found!</Route>
          </Switch>
        </Router>
      </div>
    );
  }
}

export default App;