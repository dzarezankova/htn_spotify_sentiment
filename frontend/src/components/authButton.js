import React, { Component } from "react";
import { authSignIn } from "../utils/spotify";
import { Button } from "react-bootstrap";
import "./authButton.css";

export default class AuthButton extends Component {
  render() {
    return (
      <div className="auth">
        <Button className="auth" onClick={() => authSignIn()}>
          Find Out
        </Button>
      </div>
    );
  }
}
