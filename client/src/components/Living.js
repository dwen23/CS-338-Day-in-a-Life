import React, { Component } from 'react'



export class Living extends Component {
    render() {
        return (
            <div className="card">
                <div className="card-body">
                    <p>What do you do for a living?</p>
                    
                    <select className="custom-select w-100" aria-label="Default select example" id="living" nextquestion='options'
                            defaultValue={"choose"}>
                        <option value="choose" disabled>Choose...</option>
                        <option value="high school">High School</option>
                        <option value="college">College</option>
                        <option value="work">Work</option>
                        <option value="nothing">None of the above</option>
                    </select>
                    
                </div>
                
            </div>
        )
    }
}

export default Living