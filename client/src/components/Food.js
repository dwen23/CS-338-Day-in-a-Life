import React, { Component } from 'react'

export class Food extends Component {
    render() {
        return (
            <div className="card">
                <div className="card-body">
                    What is your favorite food?
                    <input type="answer" className="form-control" id='food' nextquestion='living'></input>
                </div>
            </div>
        )
    }
}

export default Food