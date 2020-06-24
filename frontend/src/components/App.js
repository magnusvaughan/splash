import React, { Component } from "react";
import { render } from "react-dom";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import Home from "./Home";
import Phrase from "./Phrase";

class App extends Component {
  render() {
    return (
      <Switch>
        <Route path="/" component={Home} />
        <Route path="/phrase" component={Phrase} />
      </Switch>
    );
  }
}

const container = document.getElementById("app");
render(
  <Router>
    <App />
  </Router>,
  container
);

export default App;
