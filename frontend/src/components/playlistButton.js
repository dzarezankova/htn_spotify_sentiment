import React, { Component } from "react";
import { Button } from "react-bootstrap";
import { BrowserRouter as Router, Link } from "react-router-dom";
import "./playlistButton.css";

export default class PlaylistButton extends Component {
  render() {
    const message =
      this.props.sameGenre === "true" ? "Keep it Going" : "Something New";
    return (
      <div className="playlist">
        <Link
          to={{
            pathname: "/suggestion",
            state: { sameGenre: this.props.sameGenre },
          }}
        >
          <Button className="playlist">{message}</Button>
        </Link>
      </div>
    );
  }
}
