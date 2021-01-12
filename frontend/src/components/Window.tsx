import React, {Component} from "react";
import { Graph } from "react-d3-graph";
import { Box, Typography, Button, TextField, TextareaAutosize } from '@material-ui/core';

interface WindowProps {   
}

interface WindowState{
    formula: string;
    assignment: JSON;
    gamma: number;
    graphData: {
        directed: boolean,
        multigraph: boolean,
        graph: {},
        nodes: {"id": string}[],
        links: {"source": string, "target": string}[]
    }[]
}

export class Window extends Component<WindowProps, WindowState>{

  constructor(props: any) {
      super(props);
      this.state = {
        formula: '',
        assignment: JSON.parse('{}'),
        gamma: -1,
        graphData: []
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
        .then(response => response.json()).then(data => this.setState({graphData: data}))
    console.log(this.state.graphData)
  }

  adjustGraphWithoutLinks(nodes: Array<any>) {
    const newNodes : Array<any> = []
    let i : number = 0
    for (let node of nodes) {
      newNodes.push({"id": node.id, "x": i * 10, "y": i * 10})
      i++;
    }
    return newNodes
  }

  displayGraphs() {
    const myConfig = {
      nodeHighlightBehavior: true,
      node: {
        color: "lightgreen",
        size: 120,
        highlightStrokeColor: "blue",
      },
      link: {
        highlightColor: "lightblue",
      },
    };
    const graphs: Array<any> = []
    for(const [key, value] of Object.entries(this.state.graphData)) {
      let nodes: Array<any> = this.adjustGraphWithoutLinks(value.nodes)
      const links = value.links
      const data = {"nodes": nodes, "links": links}
      console.log(data)
      graphs.push(
        <Box display="flex" alignItems="center" justifyContent="center" mb={13} >
          <Typography variant="h6">T = {key}</Typography>
        </Box>,
        <Box display="flex" alignItems="center" justifyContent="center" mb={12}>
          <Graph
            id={"graph-" + key}
            data={data}
            config={myConfig}
          />
        </Box>,
        <br/>
      )
    }
    return graphs
    
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
      this.displayGraphs()
    ])
  }
}