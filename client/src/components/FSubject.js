import React, { Component } from 'react'

export class FSubject extends Component {
    render() {
        return (
            <div className="card">
                <div className="card-body">
                    What is your favorite subject?
                    <input type="answer" className="form-control" id='high school' nextquestion='lSubject'></input>
                </div>
            </div>
        )
    }
}

export default FSubject