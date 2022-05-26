import React, { Component } from 'react'

export class LSubject extends Component {
    render() {
        return (
            <div className="card">
                <div className="card-body">
                    What is your least favorite subject?
                    <input type="answer" className="form-control" id='lSubject' nextquestion='city'></input>
                </div>
            </div>
        )
    }
}

export default LSubject