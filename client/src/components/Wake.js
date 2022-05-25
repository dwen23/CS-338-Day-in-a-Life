import React, { Component } from 'react'

export class Wake extends Component {
  render() {
    return (
        <div class="card">
        <div class="card-body">
            What do you do after you wake up?
            <input type="text" class="form-control" id='wake' nextQuestion='living'></input>
        </div>
    </div>
    )
  }
}

export default Wake