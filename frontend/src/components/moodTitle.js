import React, { Component } from "react";

export default class MoodTitle extends Component {
  render() {
    const mood = this.props.mood || "unsure";
    return (
      <div className="moodTitle">
        <h1>Sounds like you've been {mood} recently,</h1>
      </div>
    );
  }
}
