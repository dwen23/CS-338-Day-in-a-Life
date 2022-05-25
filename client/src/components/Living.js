import React, { Component } from 'react'

export class Living extends Component {
    render() {
        return (
            <div class="card">
                <div class="card-body">
                    <p>What do you do for a living?</p>
                    
                    <select class="custom-select w-100" aria-label="Default select example" id="living" nextQuestion='options'>
                        <option selected>Choose...</option>
                        <option value="fSubject">High School</option>
                        <option value="major">College</option>
                        <option value="work">Work</option>
                        <option value="nothing">None of the above</option>
                    </select>
                    
                </div>
                
            </div>
        )
    }
}

export default Living