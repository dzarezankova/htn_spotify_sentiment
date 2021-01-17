import React from "react";
import "./pages.css";
import { Container, Row, Col } from "react-bootstrap";
import PlaylistWidget from "../components/playlistWidget";

export default function Suggestion() {
  return (
    <div
      className="suggestion"
      style={{ backgroundImage: `url('mainWaves.svg')` }}
    >
      <Container>
        <Row>
          <Col>
            <h1>Give these songs a play:</h1>
          </Col>
        </Row>
        <Row>
          <Col>
            <PlaylistWidget uri="playlist/37i9dQZF1DX3rxVfibe1L0" />
          </Col>
          <Col>
            <PlaylistWidget uri="playlist/37i9dQZF1DWSf2RDTDayIx" />
          </Col>
        </Row>
      </Container>
    </div>
  );
}
