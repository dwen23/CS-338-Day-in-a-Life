import React, { Component } from 'react'

export class SPronouns extends Component {
    render() {
        return (
            <div class="card">
                <div class="card-body">
                    What are your subject pronouns?
                    <input type="answer" class="form-control" id='sPronouns' nextQuestion='pPronouns'></input>
                </div>
            </div>
        )
    }
}

export default SPronouns