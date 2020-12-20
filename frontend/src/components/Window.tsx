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

  render() {
    return (
      [
        <ClauseInput submitHandler={() => this.handleRequest()}/>,
        <Graph graphData = {graphData}></Graph>
      ]
    );
  }
}