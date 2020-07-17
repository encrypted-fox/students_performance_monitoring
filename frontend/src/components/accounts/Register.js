import React, { Component } from 'react';
import { Link, Redirect } from "react-router-dom";
import "./Register.scss";
import { connect } from "react-redux";

function Register(props) {
    const svg = (
        <React.Fragment>
            <svg
                width="100"
                height="100"
                viewBox="0 0 100 100"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
                style={{
                    position: "absolute",
                    right: -50,
                }}
            >
                <circle cx="50" cy="50" r="50" fill="#202125" />
            </svg>
            <svg
                className="svg"
                width="75"
                height="75"
                viewBox="0 0 75 75"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
                onClick={() => alert("Заглушка")}
            >
                <circle cx="37.5" cy="37.5" r="37.5" fill="#16171B" />
                <path
                    d="M55 37.5L28.75 52.6554L28.75 22.3446L55 37.5Z"
                    fill="#00B275"
                />
            </svg>
        </React.Fragment>
    );

    return (
        <div className="Register">
            <h1>Register Form</h1>
            <form>
                <input placeholder="Username" type="text" />
                <hr />
                <input placeholder="Password" type="password" />
                <hr />
                <input placeholder="Password again" type="password" />
                {svg}
            </form>
            <p>
                Already have an account? <Link to="/login">Click here</Link>
            </p>
        </div>
    );
}

export default connect()(Register);