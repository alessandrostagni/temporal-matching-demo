import React, {Component} from "react";
import { Box, TextField } from '@material-ui/core';

interface GammaFormState{
    gamma?: number;
}

export class GammaForm extends Component<{}, GammaFormState> {
    render() {
        return ([
          <Box display="flex" alignItems="center" justifyContent="center" mb={8}>
            <TextField label="Gamma" onChange={(e) => {this.setState({gamma: Number(e.target.value)})}}/>
          </Box>,
        ]);
    }
}