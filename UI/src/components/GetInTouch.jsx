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
import { useRef } from 'react';  // Import useRef


export default function SignUp() {
  const formRef = useRef(0);  // Create a ref for the form
  const usernameRef = useRef('') 
  const emailRef = useRef('') 
  const passwordRef = useRef('') 
  const addressRef = useRef('') 
  const handleSubmit = async (event) => {
    event.preventDefault();
  
    try {
      const response = await fetch("http://127.0.0.1:5000/api/v1/users/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: usernameRef.current.value,
          password: passwordRef.current.value,
          email: emailRef.current.value,
          address: addressRef.current.value,
          role: "CUSTOMER",
        }),
      });
  
      const result = await response.json();
      if (response.ok) {
        console.log("Sign-up successful!");
        usernameRef.current.value = '';
        passwordRef.current.value = '';
        emailRef.current.value = '';
        addressRef.current.value = '';
        // Optionally, you can redirect the user or perform other actions on success
      } else {
        console.log("Sign-up failed:", result.message);
        // Handle sign-up failure (e.g., show an error message)
      }
    } catch (error) {
      console.error("Error during sign-up:", error);
      // Handle other errors (e.g., network issues)
    }
  };
  

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
        <form ref={formRef}
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
          <Container>
          <Typography component="h1" variant="h3" sx={{ color: "#7F4988", mb: 5, mt:7}}>
            Sign up
          </Typography>
          </Container>
          <Box component="form" noValidate onSubmit={handleSubmit}   sx={{ mt: 3, width:400} }>
            <Grid container spacing={2}>
              <Grid item xs={12} sm={6} component={motion.div} {...fadeInUp}>
                <TextField 
                  sx={{ backgroundColor:'#CDAFE4'}}
                  autoComplete="name"
                  name="username"
                  required
                  fullWidth
                  id="username"
                  label="username"
                  autoFocus
                  inputRef={usernameRef}
                />
              </Grid>
              <Grid item xs={12} sm={6} component={motion.div} {...fadeInUp}>
                <TextField                  
                  sx={{ backgroundColor:'#CDAFE4'}}
                  required
                  fullWidth
                  id="password"
                  label="password"
                  name="password"
                  type="password"
                  autoComplete="password"
                  inputRef={passwordRef}
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
                  inputRef={emailRef}
                />
              </Grid>
              <Grid item xs={12} component={motion.div} {...fadeInUp}>
                <TextField
                  sx={{ backgroundColor:'#CDAFE4'}}
                  required
                  fullWidth
                  name="address"
                  label="address"
                  id="address"
                  autoComplete="address"
                  inputRef={addressRef}

                />
              </Grid>
            </Grid>
            <Button
              type="submit"
              fullWidth
              variant="contained"
              component={motion.div} {...fadeInUp}
              sx={{ mt: 3, mb: 2, backgroundColor:'#7F4988'}}
              onClick={handleSubmit}  
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
        </form>
      </Container>
    </CustomContainer>
  );
}