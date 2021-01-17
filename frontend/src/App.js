import logo from "./logo.svg";
import React from "react";
import "./App.css";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Mood from "./pages/mood";
import Main from "./pages/main";
import Suggestion from "./pages/suggestion";

function App() {
  return (
    <div className="App">
      <Router>
        <div>
          <Switch>
            <Route path="/mood">
              <Mood />
            </Route>
            <Route path="/suggestion">
              <Suggestion />
            </Route>
            <Route path="/">
              <Main />
            </Route>
          </Switch>
        </div>
      </Router>
    </div>
  );
}

export default App;
