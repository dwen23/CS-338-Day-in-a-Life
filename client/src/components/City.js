import React, { Component } from 'react'

export class City extends Component {
    render() {
        return (
            <div className="card">
                <div className="card-body">
                    What city do you live in?
                    <input type="answer" className="form-control" id='city' nextquestion='bed'></input>
                </div>
            </div>
        )
    }
}

export default City