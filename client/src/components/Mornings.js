import React, { Component } from 'react'

export class Mornings extends Component {
    render() {
        return (
            <div class="card">
                <div class="card-body">
                    What do you do in the mornings?
                    <input type="text" class="form-control" id='mornings' nextQuestion='living'></input>
                </div>
            </div>
        )
    }
}
