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
  const passwordRef = useRef('') 
  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      console.log(
JSON.stringify({
                username: String(usernameRef.current.value),
                password: String(passwordRef.current.value),
                grant_type: "",
                scope: "",
                client_id: "",
                client_secret: "",
        })
                        )
      const response = await fetch("http://127.0.0.1:5000/api/v1/users/login",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          "Accept": "application/json",
        },
        body: new URLSearchParams({
                "username": String(usernameRef.current.value),
                "password": String(passwordRef.current.value),
                "grant_type": "password",
        }),
      });
  
      const result = await response.json();
      console.log(response)
      if (response.ok) {
        console.log("Login successful!");
        usernameRef.current.value = '';
        passwordRef.current.value = '';
        // Optionally, you can redirect the user or perform other actions on success
      } else {
        console.log("Login failed:", result.message);
        // Handle sign-up failure (e.g., show an error message)
      }
    } catch (error) {
      console.error("Error during login:", error);
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

          <Box component="form" noValidate onSubmit={handleSubmit}   sx={{ mt: 3, width:400} }>
            <Grid container spacing={2}>
              <Grid item xs={12} component={motion.div} {...fadeInUp}>
                <TextField
                  sx={{ backgroundColor:'#CDAFE4'}}
                  required
                  fullWidth
                  id="username"
                  label="Username"
                  name="username"
                  autoComplete="username"
                  inputRef={usernameRef}
                />
              </Grid>
              <Grid item xs={12} component={motion.div} {...fadeInUp}>
                <TextField
                 sx={{ backgroundColor:'#CDAFE4'}}
                 required
                 fullWidth
                 id="password"
                 label="Password"
                 name="password"
                 type="password"
                 autoComplete="password"
                 inputRef={passwordRef}
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
              Login
            </Button>
          </Box>
        </form>
      </Container>
    </CustomContainer>
  );
}
