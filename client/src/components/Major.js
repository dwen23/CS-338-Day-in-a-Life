import React, { Component } from 'react'

export class Major extends Component {
    render() {
        return (
            <div class="card">
                <div class="card-body">
                    What is your major?
                    <input type="answer" class="form-control" id='major' nextQuestion='school'></input>
                </div>
            </div>
        )
    }
}

export default Major