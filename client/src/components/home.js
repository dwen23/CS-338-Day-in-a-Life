import React, { Component } from 'react';

export class Home extends Component {
    render() {
        return (
            <div className="card">
                <div className="card-body">
                    What is your name?
                    <input type="text" className="form-control" id='name' nextquestion='sPronouns'></input>
                </div>
            </div>
        )
    }
}