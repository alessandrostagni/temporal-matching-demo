import React, {Component} from "react";
import { Box, TextareaAutosize } from '@material-ui/core';

interface AssignmentFormProps{
    onAssignmentChange: any;
}

export class AssignmentForm extends Component<AssignmentFormProps, {}> {
    render() {
        const exampleAssignment = "Example:\n" +
            "{\n" +
            "  \"w\": \"true\", \n" +
            "  \"x\": \"true\", \n" +
            "  \"y\": \"false\", \n" +
            "  \"z\": \"true\" \n" +
            "}"
        return (
            <div>
                <Box display="flex" alignItems="center" justifyContent="center" mb={1}>
                    Assignment
                </Box>
                <Box display="flex" alignItems="center" justifyContent="center" mb={8}>
                    <TextareaAutosize placeholder={exampleAssignment} rowsMin={20} rowsMax={20} style={{width:400}} onChange={(e) => {this.props.onAssignmentChange(e.target.value)}}/>
                </Box>
            </div>
        );
    }
}