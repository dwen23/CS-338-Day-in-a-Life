import React, { Component } from 'react'

export class PPronouns extends Component {
  render() {
    return (
        <div class="card">
        <div class="card-body">
            What are your possessive pronouns?
            <input type="answer" class="form-control" id='pPronouns' nextQuestion='wake'></input>
        </div>
    </div>
    )
  }
}

export default PPronouns