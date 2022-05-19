import React, { Component } from 'react'

export class Food extends Component {
    render() {
        return (
            <div class="card">
                <div class="card-body">
                    What is your favorite food?
                    <input type="answer" class="form-control" id='food' nextQuestion='fear'></input>
                </div>
            </div>
        )
    }
}

export default Food