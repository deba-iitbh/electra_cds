import React from "react";
import { Link as RouterLink } from "react-router-dom";
import { Container, Typography, Link, Box, Divider } from "@mui/material";
import styled from "@emotion/styled";
import LoginForm from "../components/LoginForm";
import { motion } from "framer-motion";

//////////////////////////////////
const RootStyle = styled("div")({
  background: "rgb(249, 250, 251)",
  height: "100vh",
  display: "grid",
  placeItems: "center",
  backgroundColor:"#CDAFE4"
});

const HeadingStyle = styled(Box)({
  textAlign: "center",
});

const ContentStyle = styled("div")({
  maxWidth: 480,
  padding: 25,
  margin: "auto",
  display: "flex",
  justifyContent: "center",
  flexDirection: "column",
  background: "#CDAFE4",
});

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

const Login = ({ setAuth }) => {
  return (
    <RootStyle >
      <Container maxWidth="sm" >
        <ContentStyle>
          <HeadingStyle component={motion.div} {...fadeInUp}>
            <Typography variant="h4" fontWeight={700} component={'p'} sx={{ color: "text.secondary", mb: 5, ml: 8}}>
              Login to your account
            </Typography>
          </HeadingStyle>

          <Box component={motion.div} {...fadeInUp}>
          </Box>

          <LoginForm setAuth={setAuth} />

          <Typography
            component={motion.p}
            {...fadeInUp}
            variant="body2"
            align="center"
            sx={{ mt: 3, color:'#7F4988'}}
          >
            Don’t have an account?{" "}
            <Link variant="subtitle2" component={RouterLink} to="/signup"  sx={{color:"#7F4988"}}>
              Sign up
            </Link>
          </Typography>
        </ContentStyle>
      </Container>
    </RootStyle>
  );
};

export default Login;