import React, {Component} from "react";
import { Button, TextField, TextareaAutosize, Grid } from '@material-ui/core';


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
      crossDomain: true,
      method: 'POST',
      headers: { 'Content-Type': 'application/json; utf-8' },
      body: JSON.stringify(this.state)
    };
    fetch('http://localhost:5000/get-graph', requestOptions)
        .then(response => console.log(response.json()))
  }

  render() {
    return ([
    <Grid container justify="center" spacing={5}>
      <Grid item xs={5}></Grid>
      <Grid item xs={2}>
        <TextField onChange={(e) => {this.setState({formula: e.target.value})}}/>
      </Grid>
      <Grid item xs={5}></Grid>

      <Grid item xs={5}></Grid>
      <Grid item xs={2}>
        <TextareaAutosize rowsMin={20} rowsMax={20} style={{width:400}} onChange={(e) => {this.setState({assignment: JSON.parse(e.target.value)})}}/>
      </Grid>
      <Grid item xs={5}></Grid>
     
      <Grid item xs={5}></Grid>
      <Grid item xs={2}>
        <TextField onChange={(e) => {this.setState({gamma: Number(e.target.value)})}}/>
      </Grid>
      <Grid item xs={5}></Grid>
      
      <Grid item xs={5}></Grid>
      <Grid item xs={2} alignItems="center">
        <Button variant="contained" color="primary" onClick={() => this.handleRequest()}>Compute!</Button>
      </Grid>
      <Grid item xs={5}></Grid>
    </Grid>
    ]);
  }
}