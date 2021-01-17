import React, { Component } from "react";

export default class PlaylistWidget extends Component {
  render() {
    const recUri = this.props.uri || "album/6QPFCq6SHAOhBI1Vf14G0y";
    return (
      <div className="playlist">
        <iframe
          src={"https://open.spotify.com/embed/" + recUri}
          width="250"
          height="330"
          frameborder="0"
          allowtransparency="true"
          allow="encrypted-media"
        ></iframe>
      </div>
    );
  }
}
