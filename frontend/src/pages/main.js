import React from "react";
import "./pages.css";
import { Container, Row, Col } from "react-bootstrap";
import AuthButton from "../components/authButton";

export default function Home() {
  return (
    <div className="main" style={{ backgroundImage: `url('mainWaves.svg')` }}>
      <Container>
        <Row>
          <Col>
            <h1>Mood On Repeat</h1>
            <p>
              How are you feeling? According to your{" "}
              <span className="highlight">Spotify</span>
            </p>
          </Col>
        </Row>
        <Row>
          <Col>
            <AuthButton />
          </Col>
        </Row>
      </Container>
    </div>
  );
}
