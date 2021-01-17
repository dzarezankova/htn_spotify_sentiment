import React from "react";
import "./pages.css";
import { Container, Row, Col, Image } from "react-bootstrap";
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
            {/* TODO Make Spotify green */}
          </Col>
        </Row>
        <Row>
          <Col>
            <AuthButton />
          </Col>
        </Row>
        {/* <Image src="mainWaves.svg" alt="Gradient Waves"></Image> */}
      </Container>
    </div>
  );
}
