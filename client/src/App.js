import './App.css';
import React from 'react';
import { Home } from './components/home'
import { Mornings } from './components/Mornings'
import { Living } from './components/Living'
import { Work } from './components/Work'
import { DoWork } from './components/DoWork'
import { Nothing } from './components/Nothing'
import { WhyNothing } from './components/WhyNothing'
import { School } from './components/School'
import { Major } from './components/Major'
import { Food } from './components/Food'
import { Fear } from './components/Fear'
import { LoadingIcon } from './components/LoadingIcon'
import { Bed } from './components/Bed'
import { City } from './components/City'
import { FSubject } from './components/FSubject'
import { Hobby } from './components/Hobby'
import { LSubject } from './components/LSubject';
import { Wake } from './components/Wake'
import { SPronouns } from './components/SPronouns'
import { PPronouns } from './components/PPronouns'

let jsonData = {};
function App() {
  const [currQuestion, setcurrQuestions] = React.useState('name');
  const [ValueA, setValueA] = React.useState("");


  function questions(index) {
    switch (index) {
      case "name":
        return (
          <Home />
        ) 
      case "wake":
        return (
          <Wake />
        )
      case "bed":
        return (
          <Bed />
        )
      case "city":
        return (
          <City />
        )
      case "high school":
        return (
          <FSubject />
        )
      case "hobby":
        return (
          <Hobby />
        )
      case "lSubject":
        return (
          <LSubject />
        )
      case "mornings":
        return (
          <Mornings />
        )
      case "living":
        return (
          <Living />
        )
      case "work":
        return (
          <Work />
        )
      case "doWork":
        return (
          <DoWork />
        )
      case "nothing":
        return (
          <Nothing />
        )
      case "whyNothing":
        return (
          <WhyNothing />
        )

      case "school":
        return (
          <School />
        )
      case "college":
        return (
          <Major />
        )
      case "food":
        return (
          <Food />
        )
      case "fear":
        return (
          <Fear />
        )
      case "sPronouns":
        return (
          <SPronouns />
        )
      case "pPronouns":
        return (
          <PPronouns />
        )
      case "done":
        return (
          <>
            {ValueA === '' ? (
              <LoadingIcon />
            ) : (
              <div>

                <h5>
                  {ValueA}
                </h5>

              </div>
            )}
          </>
        )
    }
  }

  function toNextQuestion() {
    var e = document.getElementById(currQuestion);
    var strUser = e.getAttribute('nextquestion');
    jsonData[currQuestion] = e.value;
    console.log(jsonData)
    if (strUser === 'options') {
      setcurrQuestions(e.value)
    } else {
      setcurrQuestions(strUser)
    }
  }

  function currButton() {
    if (currQuestion === 'fear') {
      return (
        <button type="submit" className="btn btn-success" onClick={submitAnswers}>
          Submit
        </button>
      )
    } else if (currQuestion === 'done') {
      return (
        <div></div>
      )
    }
    return (
      <button type="submit" className="btn btn-primary" onClick={toNextQuestion}>
        Next
      </button>
    )
  }


  function submitAnswers() {
    
    var e = document.getElementById(currQuestion);
    jsonData[currQuestion] = e.value;
    // console.log(jsonData)

    setcurrQuestions('done')

    let headers = new Headers();

    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'application/json');
    headers.append('Access-Control-Allow-Origin', 'http://localhost:3000');
    headers.append('Access-Control-Allow-Credentials', 'true');

    // Send data to the backend via POST
    fetch('http://127.0.0.1:8000/generate', {  // Enter your IP address here

      method: 'POST',
      mode: 'cors',
      headers: headers,
      body: JSON.stringify(jsonData) // body data type must match "Content-Type" header
    }).then(response => response.json()).then(data => { console.log(data); setValueA(data.text) });
  }

  return (
    <div>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossOrigin="anonymous"></link>
      <nav className="navbar navbar-dark bg-dark">
        <div className="container-fluid">
          <span className="navbar-brand mb-0 h1">Day in the Life</span>
        </div>
      </nav>

      <div>
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
      </div>

      <div className="container">
        <div className='row'>
          <div className="col">
          </div>
          <div className="col-7">
            {questions(currQuestion)}
          </div>
          <div className="col">
          </div>
        </div>

        <div>
          <br />
          <br />
          <br />
          <br />
        </div>

        <div className="row">
          <div className="col">
          </div>
          <div className="col-5">

          </div>
          <div className="col">
            {currButton()}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
