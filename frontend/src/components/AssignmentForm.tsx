import React, {Component} from "react";
import { Box, TextareaAutosize } from '@material-ui/core';

interface AssignmentFormProps{
    assignment: JSON;
    onAssignmentChange: any;
}

export class AssignmentForm extends Component<AssignmentFormProps, {}> {
    render() {
        return (
            <div>
                <Box display="flex" alignItems="center" justifyContent="center" mb={1}>
                    Assignment
                </Box>
                <Box display="flex" alignItems="center" justifyContent="center" mb={8}>
                    <TextareaAutosize defaultValue={JSON.stringify(this.props.assignment)} rowsMin={20} rowsMax={20} style={{width:400}} onChange={(e) => {this.props.onAssignmentChange(e.target.value)}}/>
                </Box>
            </div>
        );
    }
}