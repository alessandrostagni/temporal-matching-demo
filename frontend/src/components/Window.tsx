import React, {Component} from "react";
import { ClauseInput } from "./ClauseInput";
// import { Graph } from "./Graph";


interface WindowProps {   
}

interface WindowState{
    graphData: string
}

export class Window extends Component<WindowProps, WindowState>{

  constructor(props: any) {
      super(props);
      this.state = {graphData: ''}
  }

  render() {
    return (
      [
        <ClauseInput />
      ]
    );
  }
}