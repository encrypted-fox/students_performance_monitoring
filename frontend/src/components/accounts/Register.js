import React, {Component} from 'react';
import {Link, Redirect} from "react-router-dom";
import {connect} from "react-redux";
import PropTypes from "prop-types";
import {register} from "../../actions/auth";
import {createMessages} from "../../actions/messages";

class Register extends Component {
    static propTypes = {
        register: PropTypes.func.isRequired,
        isAuthenticated: PropTypes.bool
    };
    state = {
        username: '',
        email: '',
        password: '',
        password2: ''
    };

    onSubmit = e => {
        e.preventDefault();
        const {username, email, password, password2} = this.state;
        if (password !== password2) {
            this.props.createMessages({passwordNotMatch: 'Passwords do not match'});
        } else {
            const newUser = {
                email,
                username,
                password
            };
            this.props.register(newUser);
        }
    };

    onChange = e => this.setState({[e.target.name]: e.target.value});

    render() {
        if (this.props.isAuthenticated) {
            return <Redirect to='/'/>
        }
        const {username, email, password, password2} = this.state;
        return (
            <div className="col-md-6 m-auto">
                <div className="card card-body mt-5">
                    <h2 className="text-center">Регистрация</h2>
                    <form onSubmit={this.onSubmit}>
                        <div className="form-group">
                            <label>Логин</label>
                            <input
                                type="text"
                                className="form-control"
                                name="username"
                                onChange={this.onChange}
                                value={username}
                            />
                        </div>
                        <div className="form-group">
                            <label>Email</label>
                            <input
                                type="email"
                                className="form-control"
                                name="email"
                                onChange={this.onChange}
                                value={email}
                            />
                        </div>
                        <div className="form-group">
                            <label>Пароль</label>
                            <input
                                type="password"
                                className="form-control"
                                name="password"
                                onChange={this.onChange}
                                value={password}
                            />
                        </div>
                        <div className="form-group">
                            <label>Повторить пароль</label>
                            <input
                                type="password"
                                className="form-control"
                                name="password2"
                                onChange={this.onChange}
                                value={password2}
                            />
                        </div>
                        <div className="form-group">
                            <button type="submit" className="btn btn-primary">
                                Зарегистрироваться
                            </button>
                        </div>
                        <p>
                            Уже есть аккаунт? <Link to="/login">Войти</Link>
                        </p>
                    </form>
                </div>
            </div>

        );
    }
}

const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
});

export default connect(mapStateToProps, {register, createMessages})(Register);