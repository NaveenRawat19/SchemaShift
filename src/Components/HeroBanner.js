import React from 'react'
import {Box, Typography, Button} from '@mui/material'
import HeroBannerImage from '../assets/images/banner.png';
//import { padding } from '@mui/system';
const HeroBanner = () => {
  return (
    <Box sx={{
        mt: {lg: '122px', xs: '70px'},
        ml: {sm: '50px'}
    }} position="relative" p="20px">
        <Typography color="#FF2625" fontWeight="600" fontSize="26px">
            Fitness Club
        </Typography>
        <Typography fontWeight={700}
        sx = {{ fontSize: {lg: '44px', xs:'40px'}
        }}
        mb="23px" mt="30px"
        >
            Sweat, Smile <br /> ans Repeat
        </Typography>
        <Typography fontSize="22px" lineHeight="35px" mb={4}>
            Check out the most effective exercises.
        </Typography>
        <Button variant='contained' color="error" href="#Scroller"
        sx={{backgroundColor: "#ff2625", padding: "10px"}}
        >Explore Exercises</Button>
        <Typography 
        fontWeight={600}
        color="#ff2625"
        sx={{
            opacity: 0.1,
            display: {lg: 'block', xs: 'none'}
        }}
        fontSize="200px" ml={35}
        >
            Exercise</Typography>
        <img src={HeroBannerImage} alt="banner" className="hero-banner-img"></img>
    </Box>
  )
}

export default HeroBanner
