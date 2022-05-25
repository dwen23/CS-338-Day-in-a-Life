import React, { Component } from 'react'

export class Bed extends Component {
    render() {
        return (
            <div class="card">
                <div class="card-body">
                    What do you do before going to bed?
                    <input type="answer" class="form-control" id='bed' nextQuestion='hobby'></input>
                </div>
            </div>
        )
    }
}

export default Bed