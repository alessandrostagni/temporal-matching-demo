import React, {Component} from "react";
import { Box, TextField } from '@material-ui/core';

interface GammaFormProps{
  onGammaChange: any;
}


export class GammaForm extends Component<GammaFormProps, {}> {
    render() {
        return (
          <Box display="flex" alignItems="center" justifyContent="center" mb={8}>
            <TextField label="Gamma" onChange={(e) => {this.props.onGammaChange(Number(e.target.value))}}/>
          </Box>
        );
    }
}