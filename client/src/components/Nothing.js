import React, { Component } from 'react'

export class Nothing extends Component {
    render() {
        return (
            <div class="card">
                <div class="card-body">
                    What do you usually do at home?
                    <input type="answer" class="form-control" id='nothing' nextQuestion='city'></input>
                </div>
            </div>
        )
    }
}

export default Nothing