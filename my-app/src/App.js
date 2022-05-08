import './App.css';
import React from 'react'

class App extends React.Component {

  render() {
    return (

      <div class="container">
        it geets herw

        <nav class="navbar navbar-dark bg-dark fixed-top ">
          <div class="container-fluid">
            <a class="navbar-brand">Day in a Life</a>
          </div>
        </nav>
        <br />
        <br />
        <br />
        <h2>Questions</h2>
        <form>

          <label>What is your name?</label>
          <input class='form-control' type="text" ></input>
          <br/>

          <label>What do you when you wake up?</label>
          <input class='form-control' type="text" ></input>
          <br/>

          <label>What do you do during the day?</label>
            <select class="form-control" placeholder='Select'> 
              <option>High School</option>
              <option>College</option>
              <option>Work</option>
            </select>
          <br/>

          <label>Where do you study/work?</label>
          <input class='form-control' type="text" ></input>
          <br/>

          <label>What are your hobbies?</label>
          <input class='form-control' type="text" ></input>
          <br/>

          <label>What is your favorite food?</label>
          <input class='form-control' type="text" ></input>
          <br/>

          <label>What do you do before going to bed?</label>
          <input class='form-control' type="text" ></input>
          <br/>

          <button type="button" className="btn btn-primary">Submit</button>
        </form>
        <br/>

      </div>
    );
  }
}

export default App;
