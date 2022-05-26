import React, { Component } from 'react'

export class Mornings extends Component {
    render() {
        return (
            <div className="card">
                <div className="card-body">
                    What do you do in the mornings?
                    <input type="text" className="form-control" id='mornings' nextquestion='living'></input>
                </div>
            </div>
        )
    }
}
