import React, { Component } from 'react'

export class WhyNothing extends Component {
  render() {
    return (
      <div class="card">
        <div class="card-body">
          Are you retired?
          <input type="answer" class="form-control" id='whyNothing' nextQuestion='fear'></input>
        </div>
      </div>
    )
  }
}

export default WhyNothing