import React, { Component } from 'react'

export class Fear extends Component {
    render() {
        return (
            <div class="card">
                <div class="card-body">
                    What animal scares you the most?
                    <input type="answer" class="form-control" id='fear' nextQuestion='done'></input>
                </div>
            </div>

        )
    }
}

export default Fear