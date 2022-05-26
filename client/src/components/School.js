import React, { Component } from 'react'

export class School extends Component {
    render() {
        return (
            <div className="card">
                <div className="card-body">
                    Where do you go to school?
                    <input type="answer" className="form-control" id='school' nextquestion='city'></input>
                </div>
            </div>
        )
    }
}

export default School