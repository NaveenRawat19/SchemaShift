import React from 'react'
import {Box, Stack, Typography} from '@mui/material';

import Logo from '../assets/images/Logo.png'

const Footer = () => {
  return (
    <Box mt="80px" bgcolor="#fff3f4">
    <Stack gap="40px" px="40px" pt="24px" alignItems="center" justifyContent="center" mt="37px" p="0px">
      <img src={Logo} alt="logo" width="200px" height="200px" />
      <Typography variant='h5' pb="40px">
        Made with ❤️ by Naveen.
      </Typography> 
    </Stack>
    </Box>
  )
}

export default Footer
