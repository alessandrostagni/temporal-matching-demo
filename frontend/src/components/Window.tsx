import React, {Component} from "react";
import { ClauseInput } from "./ClauseInput";


interface WindowProps {
    
}

interface WindowState{
    graphData: string
}

export class Window extends Component<WindowProps, WindowState>{

  constructor(props: any) {
      super(props);
      this.state = {graphData: ''}
      //this.handleRequest = this.handleRequest.bind(this);
  }

  handleRequest() {
      this.setState({graphData: 'Clicked!'})
  }

  request_graph() {
    fetch('https://mywebsite.com/endpoint/', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        firstParam: 'yourValue',
        secondParam: 'yourOtherValue',
      })
  }

  render() {
    return (
      [
        <ClauseInput submitHandler={() => this.handleRequest()}/>,
        <Graph graphData = {graphData}></Graph>
        {userData.map((data,id)=>{
          return <div key={id}>
            <h2>{data.first_name} {data.last_name}</h2>
            <p>{data.email}</p>
          </div>
        })}
      ]
    );
  }
}