import React, {Component} from "react";
import { Box, Typography } from '@material-ui/core';

interface HeaderProps{
    text: string;
}

export class Header extends Component<HeaderProps, {}> {
    render() {
        return (
            <Box display="flex" alignItems="center" justifyContent="center" mb={13}>
                <Typography variant="h4">{this.props.text}</Typography>
            </Box>
        )
    }
}