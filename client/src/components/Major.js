import React, { Component } from 'react'

export class Major extends Component {
    render() {
        return (
            <div className="card">
                <div className="card-body">
                    What is your major?
                    <input type="answer" className="form-control" id='college' nextquestion='school'></input>
                </div>
            </div>
        )
    }
}

export default Major