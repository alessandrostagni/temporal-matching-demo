import React, {Component} from "react";

interface ClauseInputProps {
}

interface ClauseInputState {
  value : string;
  graphData: string;
}

export class ClauseInput extends Component<ClauseInputProps, ClauseInputState> {
  constructor(props: any) {
    super(props);
    this.state = {
      value: 'Please write an essay about your favorite DOM element.',
      graphData: ''
    };

  }

  render() {
  }
}