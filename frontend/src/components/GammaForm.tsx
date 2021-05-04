import React, {Component} from "react";
import { Box, TextField } from '@material-ui/core';

interface GammaFormProps{
  gamma: number;
  onGammaChange: any;
}


export class GammaForm extends Component<GammaFormProps, {}> {
    render() {
        return (
          <Box display="flex" alignItems="center" justifyContent="center" mb={8}>
            <TextField defaultValue={this.props.gamma} label="Gamma" onChange={(e) => {this.props.onGammaChange(Number(e.target.value))}}/>
          </Box>
        );
    }
}