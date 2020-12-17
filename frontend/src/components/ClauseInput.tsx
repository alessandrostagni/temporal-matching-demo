import React, {Component} from "react";

interface ClauseInputProps {
  submitHandler: Function;
}

interface ClauseInputState {
  value : string;
}

export class ClauseInput extends Component<ClauseInputProps, ClauseInputState> {
  constructor(props: any) {
    super(props);
    this.state = {
      value: 'Please write an essay about your favorite DOM element.'
    };

  }

  handleChange(event: any) {
    this.setState({value: event.target.value});
  }

  render() {
    return <button onClick={() => this.props.submitHandler} />
  }
}