import React, { Component } from 'react'

export class FSubject extends Component {
    render() {
        return (
            <div class="card">
                <div class="card-body">
                    What is your favorite subject?
                    <input type="answer" class="form-control" id='high school' nextQuestion='lSubject'></input>
                </div>
            </div>
        )
    }
}

export default FSubject