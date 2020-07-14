import React, { Component } from "react";
import { Link } from "react-router-dom";
import "./Auth.scss";
import { connect } from "react-redux";

function Auth(props) {
	const svg = (
		<svg
			onClick={() => alert("ЗоглушкА")}
			width="100"
			height="100"
			viewBox="0 0 100 100"
			fill="none"
			xmlns="http://www.w3.org/2000/svg"
			style={{
				position: "absolute",
					alignSelf: "flex-end",
					marginLeft: 50,
					cursor: "pointer",
				}}
			>
				<circle cx="50" cy="50" r="50" fill="#202125" />
				<circle cx="49.5" cy="49.5" r="37.5" fill="#16171B" />
				<path
					d="M67 49.5L40.75 64.6554L40.75 34.3446L67 49.5Z"
					fill="#00B275"
				/>
			</svg>
		);
		return (
			<div className="Auth">
				<h1>Sign In Form</h1>
				<form>
					<input placeholder="username" type="text"/>
					<hr/>
					<input placeholder="password" type="password"/>
					{svg}
				</form>
				<p>
					Don’t have an account? <Link to="/register">Click here</Link>
				</p>
			</div>
		);
}

export default connect()(Auth);
