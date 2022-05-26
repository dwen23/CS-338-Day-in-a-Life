import React, { Component } from 'react'

export class DoWork extends Component {
    render() {
        return (
            <div className="card">
                <div className="card-body">
                    What is a common task you have at work?
                    <input type="answer" className="form-control" id='doWork' nextquestion='city'></input>
                </div>
            </div>
        )
    }
}

export default DoWork