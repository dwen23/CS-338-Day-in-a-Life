import React, { Component } from 'react'

export class Nothing extends Component {
    render() {
        return (
            <div class="card">
                <div class="card-body">
                    Do you have any plans for the future?
                    <input type="answer" class="form-control" id='nothing' nextQuestion='whyNothing'></input>
                </div>
            </div>
        )
    }
}

export default Nothing