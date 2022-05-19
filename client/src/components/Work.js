import React, { Component } from 'react'

export class Work extends Component {
    render() {
        return (
            <div class="card">
                <div class="card-body">
                    Where do you work?
                    <input type="answer" class="form-control" id='work' nextQuestion='doWork'></input>
                </div>
            </div>
        )
    }
}

export default Work