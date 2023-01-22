import * as React from 'react';

import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';

export default function OutlinedCard({content}) {
    return (
      <Box sx={{ minWidth: 275, mr: '1vw', ml: '1vw'}}>
        <Card variant="outlined">
          <CardContent>
        <Typography>
            {content}
        </Typography>
      </CardContent>
      <CardActions>
        <Button size="small">Learn More</Button>
      </CardActions>
      </Card>
      </Box>
    );
  }


