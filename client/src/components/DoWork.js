import React, { Component } from 'react'

export class DoWork extends Component {
    render() {
        return (
            <div class="card">
                <div class="card-body">
                    What do you do when you work?
                    <input type="answer" class="form-control" id='doWork' nextQuestion='fear'></input>
                </div>
            </div>
        )
    }
}

export default DoWork