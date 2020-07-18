import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import './Auth.scss';
import {connect} from 'react-redux';

function Auth(props) {
    const svg = (
        <React.Fragment>
            <svg
                width='100'
                height='100'
                viewBox='0 0 100 100'
                fill='none'
                xmlns='http://www.w3.org/2000/svg'
                style={{
                    position: 'absolute',
                    right: -50,
                }}>
                <circle cx='50' cy='50' r='50' fill='#202125'/>
            </svg>
            <svg
                className='svg'
                width='75'
                height='75'
                viewBox='0 0 75 75'
                fill='none'
                xmlns='http://www.w3.org/2000/svg'
                onClick={() => alert('Заглушка')}>
                <circle cx='37.5' cy='37.5' r='37.5' fill='#16171B'/>
                <path
                    d='M55 37.5L28.75 52.6554L28.75 22.3446L55 37.5Z'
                    fill='#00B275'
                />
            </svg>
        </React.Fragment>
    );

    return (
        <div className='Auth'>
            <h1>Sign In Form</h1>
            <form>
                <input placeholder='username' type='text'/>
                <hr/>
                <input placeholder='password' type='password'/>
                {svg}
            </form>
            <p>
                Don’t have an account? <Link to='/register'>Click here</Link>
            </p>
        </div>
    );
}

export default connect()(Auth);
