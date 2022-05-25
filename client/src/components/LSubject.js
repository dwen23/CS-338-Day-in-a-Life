import React, { Component } from 'react'

export class LSubject extends Component {
    render() {
        return (
            <div class="card">
                <div class="card-body">
                    What is your least favorite subject?
                    <input type="answer" class="form-control" id='lSubject' nextQuestion='city'></input>
                </div>
            </div>
        )
    }
}

export default LSubject