import axios from 'axios';
import {createMessages, returnErrors} from "./messages";
import {tokenConfig} from "./auth";

import {ADD_EMPLOYEE, DELETE_EMPLOYEE, EDIT_EMPLOYEE, GET_EMPLOYEES} from "./types";

export const getEmployees = () => (dispatch, getState) => {
    axios.get('/api/employees/', tokenConfig(getState))
        .then(res => {
            dispatch({
                type: GET_EMPLOYEES,
                payload: res.data
            });
        })
        .catch(err => dispatch(returnErrors(err.response.data, err.response.status)));

};

export const deleteEmployee = (id) => (dispatch, getState) => {
    axios.delete(`/api/employees/${id}/`, tokenConfig(getState))
        .then(res => {
            dispatch(createMessages({deleteEmployee: 'Employee Deleted'}));
            dispatch({
                type: DELETE_EMPLOYEE,
                payload: id
            });
        })
        .catch(err => console.log(err));
};

export const addEmployee = (employee) => (dispatch, getState) => {
    axios.post("/api/employees/", employee, tokenConfig(getState))
        .then(res => {
            dispatch(createMessages({addEmployee: 'Employee Added'}));
            dispatch({
                type: ADD_EMPLOYEE,
                payload: res.data
            });
        })
        .catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
};

export const editEmployee = (id, employee) => (dispatch, getState) => {
    axios.put(`/api/employees/${id}/`, employee, tokenConfig(getState))
        .then(res => {
            dispatch(createMessages({editEmloyee: 'Employee Edited'}));
            dispatch({
                type: EDIT_EMPLOYEE,
                payload: res.data
            });
        })
        .catch(err => dispatch(returnErrors(err.response.data, err.response.status)));
};
