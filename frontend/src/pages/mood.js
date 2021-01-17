import React from "react";
import "./pages.css";
import { Container, Row, Col } from "react-bootstrap";
import PlaylistButton from "../components/playlistButton";
import MoodTitle from "../components/moodTitle";

export default function Mood() {
  return (
    <div className="mood" style={{ backgroundImage: `url('moodWaves.svg')` }}>
      <Container>
        <Row>
          <Col>
            <MoodTitle mood="feeling down" />
          </Col>
        </Row>
        <Row>
          <Col>
            <PlaylistButton sameGenre="true" />
          </Col>
          <Col>
            <PlaylistButton sameGenre="false" />
          </Col>
        </Row>
      </Container>
    </div>
  );
}
