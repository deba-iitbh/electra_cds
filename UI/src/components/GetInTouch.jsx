import * as React from 'react';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import styled from '@emotion/styled';
import { motion } from "framer-motion";


export default function SignUp() {
  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    console.log({
      email: data.get('email'),
      password: data.get('password'),
    });
  }

  const CustomContainer = styled(Container)({
    backgroundColor: '#CDAFE4',
    height : '600',
    width : '400',
    display: 'flex',

  })

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
  


  return (
    <CustomContainer maxWidth="xl">
      <Container component="main" maxWidth="xs" >
        <CssBaseline />
        <Box 
          component={motion.div} {...fadeInUp}
          sx={{
            marginTop: 15,
            height: "80vh",
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            placeItems: "center",

          }}
        >
          <Typography component="h1" variant="h4" sx={{ color: "#7F4988", mb: 5}}>
            Sign up
          </Typography>
          <Box component="form" noValidate onSubmit={handleSubmit}   sx={{ mt: 3, width:400} }>
            <Grid container spacing={2}>
              <Grid item xs={12} sm={6} component={motion.div} {...fadeInUp}>
                <TextField 
                  sx={{ backgroundColor:'#CDAFE4'}}
                  autoComplete="given-name"
                  name="firstName"
                  required
                  fullWidth
                  id="firstName"
                  label="First Name"
                  autoFocus
                />
              </Grid>
              <Grid item xs={12} sm={6} component={motion.div} {...fadeInUp}>
                <TextField                  
                  sx={{ backgroundColor:'#CDAFE4'}}
                  required
                  fullWidth
                  id="lastName"
                  label="Last Name"
                  name="lastName"
                  autoComplete="family-name"
                />
              </Grid>
              <Grid item xs={12} component={motion.div} {...fadeInUp}>
                <TextField
                  sx={{ backgroundColor:'#CDAFE4'}}
                  required
                  fullWidth
                  id="email"
                  label="Email Address"
                  name="email"
                  autoComplete="email"
                />
              </Grid>
              <Grid item xs={12} component={motion.div} {...fadeInUp}>
                <TextField
                  sx={{ backgroundColor:'#CDAFE4'}}
                  required
                  fullWidth
                  name="password"
                  label="Password"
                  type="password"
                  id="password"
                  autoComplete="new-password"
                />
              </Grid>
            </Grid>
            <Button
              type="submit"
              fullWidth
              variant="contained"
              component={motion.div} {...fadeInUp}
              sx={{ mt: 3, mb: 2, backgroundColor:'#7F4988'}}
            >
              Sign Up
            </Button>
            <Grid container justifyContent="flex-end" >
              <Grid item>
                <Link href="#" variant="body2" sx={{ color: '#7F4988'}}>
                  Already have an account? Log in
                </Link>
              </Grid>
            </Grid>
          </Box>
        </Box>
      </Container>
    </CustomContainer>
  );
}