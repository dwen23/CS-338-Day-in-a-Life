import React, { Component } from 'react'

export class PPronouns extends Component {
  render() {
    return (
        <div className="card">
        <div className="card-body">
            What are your possessive pronouns?
            <input type="answer" className="form-control" id='pPronouns' nextquestion='wake'></input>
        </div>
    </div>
    )
  }
}

export default PPronouns