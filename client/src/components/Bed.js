import React, { Component } from 'react'

export class Bed extends Component {
    render() {
        return (
            <div className="card">
                <div className="card-body">
                    What do you do before going to bed?
                    <input type="answer" className="form-control" id='bed' nextquestion='hobby'></input>
                </div>
            </div>
        )
    }
}

export default Bed