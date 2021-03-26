import React, {Component} from "react";
import ForceGraph2D from 'react-force-graph-2d';
import { Box, Typography } from '@material-ui/core';
import { handleRequest} from '../api/api';

import { MainTitle } from './MainTitle';
import { Header } from './Header';
import { FormulaForm } from './FormulaForm';
import { AssignmentForm } from './AssignmentForm';
import { GammaForm } from './GammaForm';
import { SubmitButton } from "./SubmitButton";


interface WindowState{
    formula: string;
    assignment: JSON;
    gamma: number;
    linkStreamData: {
        directed: boolean,
        multigraph: boolean,
        graph: {},
        nodes: {"id": string}[],
        links: {"source": string, "target": string}[]
    }[];
    matchingData: {
      directed: boolean,
      multigraph: boolean,
      graph: {},
      nodes: {"id": string}[],
      links: {"source": string, "target": string}[]
  }[]
}

export class Window extends Component<{}, WindowState>{

  constructor(props: any) {
    super(props);
    this.state = {
      formula: '',
      assignment: JSON.parse('{}'),
      gamma: -1,
      linkStreamData: [],
      matchingData: []
    }
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
      newNodes.push({"id": node.id, "name": node.id, "x": x + cx, "y": y0, "color": "blue"})
      x = x + increment
      i++;
    }
    return newNodes
  }

  displayGraphs(data: {
    directed: boolean,
    multigraph: boolean,
    graph: {},
    nodes: {"id": string}[],
    links: {"source": string, "target": string}[]
    }[]
  ) {
    const graphs: Array<any> = []
    for(const [key, value] of Object.entries(data)) {
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
    return (
      <div>
        <MainTitle/>
        <FormulaForm onFormulaChange={(formula: string) => {this.setState({formula: formula})}}/>
        <AssignmentForm onAssignmentChange={(assignment: string) => {this.setState({assignment: JSON.parse(assignment)})}}/>
        <GammaForm onGammaChange={(gamma: number) => {this.setState({gamma: gamma})}}></GammaForm>
        <SubmitButton handlerParent={this} onButtonClick={handleRequest} />
        <br/>
        <br/>
        <Header text='Link Stream'/>
        {this.displayGraphs(this.state.linkStreamData)}
        <br/>
        <br/>
        <Header text='Matching'/>
        {this.displayGraphs(this.state.matchingData)}
      </div>
    )
  }
}