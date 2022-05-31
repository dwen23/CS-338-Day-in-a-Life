import React, { Component } from 'react'

export class Wake extends Component {
  render() {
    return (
        <div className="card">
        <div className="card-body">
            What do you do after you wake up?
            <input type="text" className="form-control" id='wake' nextquestion='food'></input>
        </div>
    </div>
    )
  }
}

export default Wake