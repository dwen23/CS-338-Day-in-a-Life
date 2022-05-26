import React, { Component } from 'react'

export class WhyNothing extends Component {
  render() {
    return (
      <div className="card">
        <div className="card-body">
          Are you retired?
          <input type="answer" className="form-control" id='whyNothing' nextquestion='fear'></input>
        </div>
      </div>
    )
  }
}

export default WhyNothing