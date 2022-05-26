import React, { Component } from 'react'

export class SPronouns extends Component {
    render() {
        return (
            <div className="card">
                <div className="card-body">
                    What are your subject pronouns?
                    <input type="answer" className="form-control" id='sPronouns' nextquestion='pPronouns'></input>
                </div>
            </div>
        )
    }
}

export default SPronouns