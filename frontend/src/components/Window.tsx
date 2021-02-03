import React, {Component} from "react";
import ForceGraph2D from 'react-force-graph-2d';
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
    const REACT_APP_API_URL: any = process.env['REACT_APP_API_URL'];
    fetch(REACT_APP_API_URL, requestOptions)
        .then(response => response.json()).then(data => this.setState({graphData: data}))
    console.log(this.state.graphData)
  }

  adjustNodes(nodes: Array<any>) {
    const newNodes : Array<any> = []
    const cx = 400
    const cy = 200
    const r = 150
    let i: number = 0
    const increment = 2*r / nodes.length
    let x : number = -r

    for (let node of nodes) {
      const y = Math.sqrt(r**2 - x**2)
      let y0: number;
      if (i % 2 === 0) {
        y0 = cy + y
      } else {
        y0 = cy - y
      }
      newNodes.push({"id": node.id, "name": node.id, "x": x + cx, "y": y0, "color": "red"})
      x = x + increment
      i++;
    }
    return newNodes
  }

  displayGraphs() {
    const graphs: Array<any> = []
    for(const [key, value] of Object.entries(this.state.graphData)) {
      let nodes: Array<any> = this.adjustNodes(value.nodes)
      const links = value.links
      const data = {"nodes": nodes, "links": links}
      graphs.push(
        <Box display="flex" alignItems="center" justifyContent="center" mb={13} >
          <Typography variant="h6">T = {key}</Typography>
        </Box>,
        <Box display="flex" alignItems="center" justifyContent="center" mb={12}>
          <ForceGraph2D
            nodeId="id"
            graphData={data}
            nodeCanvasObject={(node: any, ctx, globalScale) => {
              const label: any = node.id;
              const fontSize = 12/globalScale;

              ctx.font = `${fontSize}px Sans-Serif`;  
              ctx.textAlign = 'center';
              ctx.textBaseline = 'middle';
              ctx.fillStyle = "black";
              ctx.fillText(label, node.x , node.y + 10);
              ctx.fillStyle = node.color;
              ctx.beginPath();
              ctx.arc(node.x, node.y, 5, 0, 2 * Math.PI, false);
              ctx.fill();
            }}
          />
        </Box>,
        <br/>
      )
    }
    return graphs
    
  }

  render() {
    const exampleAssignment = "Example:\n" +
    "{\n" +
      "  \"w\": \"true\", \n" +
      "  \"x\": \"true\", \n" +
      "  \"y\": \"false\", \n" +
      "  \"z\": \"true\" \n" +
    "}"

    return ([
      <Box display="flex" alignItems="center" justifyContent="center" mb={13} >
        <Typography variant="h3">Temporal matching from clause</Typography>
      </Box>,
      <Box display="flex" alignItems="center" justifyContent="center" mb={8}>
        <TextField label="Clause" helperText="e.g. (x or y) and (y or z)" onChange={(e) => {this.setState({formula: e.target.value})}}/>
      </Box>,
      <Box display="flex" alignItems="center" justifyContent="center" mb={1}>
        Assignment
      </Box>,
      <Box display="flex" alignItems="center" justifyContent="center" mb={8}>
        <TextareaAutosize placeholder={exampleAssignment} rowsMin={20} rowsMax={20} style={{width:400}} onChange={(e) => {this.setState({assignment: JSON.parse(e.target.value)})}}/>
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