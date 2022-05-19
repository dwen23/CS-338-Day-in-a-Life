import React, { Component } from 'react';

export class Home extends Component {
    render() {
        return (
            <div class="card">
                <div class="card-body">
                    What is your name?
                    <input type="text" class="form-control" id='name' nextQuestion='mornings'></input>
                </div>
            </div>
        )
    }
}