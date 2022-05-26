import React, { Component } from 'react'

export class Hobby extends Component {
    render() {
        return (
            <div className="card">
                <div className="card-body">
                    What is your favorite hobby?
                    <input type="answer" className="form-control" id='hobby' nextquestion='fear'></input>
                </div>
            </div>
        )
    }
}

export default Hobby