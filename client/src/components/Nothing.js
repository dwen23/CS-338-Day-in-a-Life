import React, { Component } from 'react'

export class Nothing extends Component {
    render() {
        return (
            <div className="card">
                <div className="card-body">
                    What do you usually do at home?
                    <input type="answer" className="form-control" id='nothing' nextquestion='city'></input>
                </div>
            </div>
        )
    }
}

export default Nothing