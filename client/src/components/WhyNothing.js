import React, { Component } from 'react'

export class WhyNothing extends Component {
  render() {
    return (
      <div class="card">
        <div class="card-body">
          Why are you currently doing nothing?
          <input type="answer" class="form-control" id='whyNothing' nextQuestion='fear'></input>
        </div>
      </div>
    )
  }
}

export default WhyNothing