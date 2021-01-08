import React, {Component} from "react";
import { Graph } from "./Graph";
import { Box, Typography, Button, TextField, TextareaAutosize } from '@material-ui/core';


interface WindowProps {   
}

interface WindowState{
    formula: string;
    assignment: JSON
    gamma: number;
    graphData: string;
}

export class Window extends Component<WindowProps, WindowState>{

  constructor(props: any) {
      super(props);
      this.state = {
        formula: '',
        assignment: JSON.parse('{}'),
        gamma: -1,
        graphData: ''
      }
  }

  handleRequest() {
    const requestOptions = {
      crossDomain: true,
      method: 'POST',
      headers: { 'Content-Type': 'application/json; utf-8' },
      body: JSON.stringify({
        formula: this.state.formula,
        assignment: this.state.assignment,
        gamma: this.state.gamma
      })
    };
    fetch('http://localhost:5000/get-graph', requestOptions)
        .then(response => response.json()).then(data => this.setState({graphData: JSON.stringify(data)}))
    this.render()
  }

  render() {
    return ([
      <Box display="flex" alignItems="center" justifyContent="center" mb={13} >
        <Typography variant="h3">Temporal matching from clause</Typography>
      </Box>,
      <Box display="flex" alignItems="center" justifyContent="center" mb={8}>
        <TextField label="Clause" onChange={(e) => {this.setState({formula: e.target.value})}}/>
      </Box>,
      <Box display="flex" alignItems="center" justifyContent="center" mb={1}>
        Assignment
      </Box>,
      <Box display="flex" alignItems="center" justifyContent="center" mb={8}>
        <TextareaAutosize rowsMin={20} rowsMax={20} style={{width:400}} onChange={(e) => {this.setState({assignment: JSON.parse(e.target.value)})}}/>
      </Box>,
      <Box display="flex" alignItems="center" justifyContent="center" mb={8}>
        <TextField label="Gamma" onChange={(e) => {this.setState({gamma: Number(e.target.value)})}}/>
      </Box>,
      <Box display="flex" alignItems="center" justifyContent="center">
        <Button variant="contained" color="primary" onClick={() => this.handleRequest()}>Compute!</Button>
      </Box>,
      <Graph graphData={this.state.graphData}/>
    ]);
  }
}