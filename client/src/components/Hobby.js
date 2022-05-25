import React, { Component } from 'react'

export class Hobby extends Component {
    render() {
        return (
            <div class="card">
                <div class="card-body">
                    What is your favorite hobby?
                    <input type="answer" class="form-control" id='hobby' nextQuestion='fear'></input>
                </div>
            </div>
        )
    }
}

export default Hobby