import {Component} from "react";


interface GraphProps {
    graphData: string;
}

interface GraphState {   
}

export class Graph extends Component<GraphProps, GraphState>{

  render() {
    return ([
      this.props.graphData
    ]);
  }
}