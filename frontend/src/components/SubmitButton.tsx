import React, {Component} from "react";
import { Box, Button } from '@material-ui/core';


interface SubmitButtonProps{
    handlerParent: any;
    onButtonClick: any;
}


export class SubmitButton extends Component<SubmitButtonProps, {}> {
    render() {
        return (
            <div>
                <Box display="flex" alignItems="center" justifyContent="center">
                    <Button variant="contained" color="primary" onClick={(e) => {this.props.onButtonClick(this.props.handlerParent)}}>Compute!</Button>
                </Box>
            </div>
        );
    }
}