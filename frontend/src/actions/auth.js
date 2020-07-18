import axios from 'axios';
import {returnErrors} from './messages';

import {
    LOGIN_FAIL,
    LOGIN_SUCCESS,
    LOGOUT_SUCCESS,
    REGISTER_FAIL,
    REGISTER_SUCCESS,
} from './types';

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === name + '=') {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }
    return cookieValue;
}

export const login = (username, password) => (dispatch) => {
    const csrftoken = getCookie('csrftoken');
    const config = {
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
    };

    const body = JSON.stringify({username, password});

    axios
        .post('/authentication/token/', body, config)
        .then((res) => {
            dispatch({
                type: LOGIN_SUCCESS,
                username: username,
                payload: res.data,
            });
        })
        .catch((err) => {
            dispatch(returnErrors(err.response.data, err.response.status));
            dispatch({
                type: LOGIN_FAIL,
            });
        });
};

export const register = ({username, password, email}) => (dispatch) => {
    const csrftoken = getCookie('csrftoken');
    const config = {
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
    };

    const body = JSON.stringify({username, password, email});

    axios
        .post('/authentication/register/', body, config)
        .then((res) => {
            dispatch({
                type: REGISTER_SUCCESS,
                username: username,
                payload: res.data,
            });
        })
        .catch((err) => {
            dispatch(returnErrors(err.response.data, err.response.status));
            dispatch({
                type: REGISTER_FAIL,
            });
        });
};

export const logout = () => (dispatch, getState) => {
    const body = JSON.stringify({token: getState().auth.access_token});

    axios
        .post('/authentication/token/revoke/', body, tokenConfig(getState))
        .then((res) => {
            dispatch({
                type: LOGOUT_SUCCESS,
                payload: res.data,
            });
        })
        .catch((err) => {
            dispatch(returnErrors(err.response.data, err.response.status));
        });
};

export const tokenConfig = (getState) => {
    const csrftoken = getCookie('csrftoken');
    const token = getState().auth.access_token;

    const config = {
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
    };

    if (token) {
        config.headers['Authorization'] = `Bearer ${token}`;
    }

    return config;
};
