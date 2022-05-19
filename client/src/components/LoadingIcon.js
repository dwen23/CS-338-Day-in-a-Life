import React, { Component } from 'react'
import logo from '../icons/48x48.gif'

export class LoadingIcon extends Component {
  render() {
    return (
      <div class='d-flex justify-content-center'>
        <h2>Creating a day in YOUR life...</h2>
        <img src={logo}></img>
      </div>
    )
  }
}

export default LoadingIcon