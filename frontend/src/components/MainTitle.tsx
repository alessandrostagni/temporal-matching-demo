import React, {Component} from "react";
import { Box, Typography } from '@material-ui/core';


export class MainTitle extends Component {
    render() {
        return ([
            <Box display="flex" alignItems="center" justifyContent="center" mb={13}>
                <Typography variant="h3">Temporal matching from clause</Typography>
            </Box>
        ])
    }
}