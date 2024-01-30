import React from 'react'
import pic1 from '../components/pic1.png'
import pic2 from '../components/pic2.png'
import pic3 from '../components/pic3.png'
import pic4 from '../components/pic4.png'

import {  
    Grid, 
    Typography,
    Card,
    CardContent,
    Box,
} from "@mui/material";
import styled from '@emotion/styled'
import { Image } from 'react-bootstrap'
import { motion } from "framer-motion";


let easing = [0.6, -0.05, 0.01, 0.99];
const fadeInUp = {
  initial: {
    y: 60,
    opacity: 0,
    transition: { duration: 0.6, ease: easing },
  },
  animate: {
    y: 0,
    opacity: 1,
    transition: {
      duration: 0.6,
      ease: easing,
    },
  },
};

const Cimg = styled(Image)
({
   borderRadius:'15',
   borderColor:'white'
});

const CustomContainer = styled(Box)({
    backgroundColor:'#D4BEE5',
    height : '500',
    width:'2000',
    alignItems:'center'

})

const Content = () => {
  return (    
    <CustomContainer>
        <Grid px={5}
                py={5}><Typography component={motion.p} {...fadeInUp} color='#7F4988' fontSize={40} fontWeight={700} ml={65} mt={10}>'What are we offering ?'</Typography></Grid>
            <Grid display='flex' >
                <Card
                component={motion.div} {...fadeInUp}
                sx={{
                    minHeight: 200,
                    width: 200,
                    m: 8,
                    ml: 20,
                    flexDirection:'row',
                    justifyContent: 'center',
                    alignItems: 'center',
                    textAlign: 'center',
                    border: '1px solid #ccc',
                }}>
                    <CardContent>
                        <Cimg src={pic1} width={100}></Cimg>
                        <Typography 
                        variant="h8" 
                        component="p"
                        sx={{
                            fontWeight: 700,
                            textTransform: 'capitalize',
                            mt:3,
                            color: '#7F4988'
                        }}
                        >
                          DELIVERING AT YOUR DOORSTEP
                        </Typography>
                    </CardContent>
                </Card>
            

                <Card 
                component={motion.div} {...fadeInUp}
                sx={{ 
                    minHeight: 200,
                    width: 200,
                    m: 8,
                    flexDirection:'row',
                    justifyContent: 'center',
                    alignItems: 'center',
                    textAlign: 'center', 
                    border: '1px solid #ccc'
                }}>
                    <CardContent>
                    <Cimg src={pic2} width={100} height={100} borderRadius='50' borderColor='white'></Cimg>

                        <Typography 
                        variant="h8" 
                        component="p"
                        sx={{
                            fontWeight: 700,
                            textTransform: 'capitalize',
                            mt:3,
                            color: '#7F4988'
                        }}
                        >
                        QUALITY
                        </Typography>
                    </CardContent>
                </Card>

                <Card 
                component={motion.div} {...fadeInUp}
                sx={{ 
                    minHeight: 200,
                    width: 200,
                    m: 8,
                    justifyContent: 'center',
                    flexDirection:'row',
                    alignItems: 'center',
                    textAlign: 'center', 
                    border: '1px solid #ccc'
                }}>
                    <CardContent>
                    <Cimg src={pic3} width={100} borderRadius='50' borderColor='white'></Cimg>

                        <Typography 
                        variant="h8" 
                        component="p"
                        sx={{
                            fontWeight: 700,
                            textTransform: 'capitalize',
                            mt:3,
                            color: '#7F4988'
                        }}
                        >
                        STUDENT DISCOUNT
                        </Typography>
                    </CardContent>
                </Card>

                <Card 
                component={motion.div} {...fadeInUp}
                sx={{ 
                    minHeight: 200,
                    width: 200,
                    m: 8,
                    justifyContent: 'center',
                    flexDirection:'row',
                    alignItems: 'center',
                    textAlign: 'center',                    
                    border: '1px solid #ccc',
                }}
                >
                    <CardContent>
                    <Cimg src={pic4} width={100} borderRadius='50' borderColor='white'></Cimg>
                        <Typography 
                        variant="h8" 
                        component="p"
                        sx={{
                            fontWeight: 700,
                            textTransform: 'capitalize',
                            mt:3,
                            color: '#7F4988'
                        }}
                        >
                        WIDE RANGE OF PRODUCTS
                        </Typography>
                    </CardContent>
                </Card>
            </Grid>
            </CustomContainer>
    );
}

export default Content