import React, { Component } from 'react'

export class DoWork extends Component {
    render() {
        return (
            <div class="card">
                <div class="card-body">
                    What is a common task you have at work?
                    <input type="answer" class="form-control" id='doWork' nextQuestion='city'></input>
                </div>
            </div>
        )
    }
}

export default DoWork