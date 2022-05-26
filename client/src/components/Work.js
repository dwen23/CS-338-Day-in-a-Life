import React, { Component } from 'react'

export class Work extends Component {
    render() {
        return (
            <div className="card">
                <div className="card-body">
                    Where do you work?
                    <input type="answer" className="form-control" id='work' nextquestion='doWork'></input>
                </div>
            </div>
        )
    }
}

export default Work