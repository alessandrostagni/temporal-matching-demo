import React, {Component} from "react";
import { Box, TextareaAutosize } from '@material-ui/core';

interface AssignmentFormState{
    exampleAssignment: string;
    assignment?: string;
}

export class AssignmentForm extends Component<{}, AssignmentFormState> {
    
    constructor(props: any) {
        super(props);
        this.state = {
            exampleAssignment: "Example:\n" +
                "{\n" +
                "  \"w\": \"true\", \n" +
                "  \"x\": \"true\", \n" +
                "  \"y\": \"false\", \n" +
                "  \"z\": \"true\" \n" +
                "}"
            }
        }

    render() {
        return ([
            <Box display="flex" alignItems="center" justifyContent="center" mb={1}>
                Assignment
            </Box>,
            <Box display="flex" alignItems="center" justifyContent="center" mb={8}>
                <TextareaAutosize placeholder={this.state.exampleAssignment} rowsMin={20} rowsMax={20} style={{width:400}} onChange={(e) => {this.setState({assignment: JSON.parse(e.target.value)})}}/>
            </Box>,
        ]);
    }
}