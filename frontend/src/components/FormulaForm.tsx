import React, {Component} from "react";
import { Box, TextField } from '@material-ui/core';

interface FormulaFormProps{
    onFormulaChange: any;
}

export class FormulaForm extends Component<FormulaFormProps, {}> {
    render() {
        return ([
            <Box display="flex" alignItems="center" justifyContent="center" mb={8}>
                <TextField label="Clause" helperText="e.g. (x or y) and (y or z)" onChange={(e) => {this.props.onFormulaChange(e.target.value)}}/>
            </Box>,
        ]);
    }
}