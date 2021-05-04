import React, {Component} from "react";
import { Box, TextField } from '@material-ui/core';

interface FormulaFormProps{
    formula: string;
    onFormulaChange: any;
}

export class FormulaForm extends Component<FormulaFormProps, {}> {
    render() {
        return (
            <Box display="flex" alignItems="center" justifyContent="center" mb={8}>
                <TextField label="Clause" defaultValue={this.props.formula} onChange={(e) => {this.props.onFormulaChange(e.target.value)}}/>
            </Box>
        );
    }
}