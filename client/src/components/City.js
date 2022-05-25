import React, { Component } from 'react'

export class City extends Component {
    render() {
        return (
            <div class="card">
                <div class="card-body">
                    What city do you live in?
                    <input type="answer" class="form-control" id='city' nextQuestion='food'></input>
                </div>
            </div>
        )
    }
}

export default City