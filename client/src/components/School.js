import React, { Component } from 'react'

export class School extends Component {
    render() {
        return (
            <div class="card">
                <div class="card-body">
                    Where do you go to school?
                    <input type="answer" class="form-control" id='school' nextQuestion='city'></input>
                </div>
            </div>
        )
    }
}

export default School