import React, { Component } from 'react'

export class Fear extends Component {
    render() {
        return (
            <div className="card">
                <div className="card-body">
                    What animal scares you the most?
                    <input type="answer" className="form-control" id='fear' nextquestion='done'></input>
                </div>
            </div>

        )
    }
}

export default Fear