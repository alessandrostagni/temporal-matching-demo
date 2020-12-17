import React, {Component} from "react";
import { ClauseInput } from "./ClauseInput";


interface WindowProps {
    
}

interface WindowState{
    data: string
}

export class Window extends Component<WindowProps, WindowState>{

  constructor(props: any) {
      super(props);
      this.state = {data: ''}
      this.handleRequest = this.handleRequest.bind(this);
  }

  handleRequest() {
      this.setState({data: 'Clicked!'})
  }

  render() {
    return (
      <div>
        <ClauseInput
        submitHandler={() => this.handleRequest()}
      />
      {this.state.data}
      </div>
    );
  }
}