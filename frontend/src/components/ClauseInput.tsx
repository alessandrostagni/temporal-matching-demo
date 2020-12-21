import React, {Component} from "react";
import { Button, TextField } from '@material-ui/core';


interface ClauseInputProps {
}

interface ClauseInputState {
  formula: string;
  assignment: JSON
  gamma: number;
}

export class ClauseInput extends Component<ClauseInputProps, ClauseInputState> {
  constructor(props: any) {
    super(props);
    this.state = {
      formula: '',
      assignment: JSON.parse('{}'),
      gamma: -1
    };

  }

  handleRequest() {
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(this.state)
    };
    fetch('https://localhost:3000/get-graph', requestOptions)
        .then(response => console.log(response.json()))
  }

  render() {
    return ([
      <TextField style={{display: 'inline'}} onChange={(e) => {this.setState({formula: e.target.value})}}/>,
      <br/>,
      <TextField style={{display: 'inline'}} onChange={(e) => {this.setState({assignment: JSON.parse(e.target.value)})}}/>,
      <br/>,
      <TextField style={{display: 'inline'}} onChange={(e) => {this.setState({gamma: Number(e.target.value)})}}/>,
      <br/>,
      <Button variant="contained" color="primary" onClick={() => this.handleRequest()}>Compute!</Button>
    ]);
  }
}