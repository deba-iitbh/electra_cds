import React from'react';
//rotas
import {BrowserRouter, Routes, Route} from 'react-router-dom';
//pages
import Home from './pages/Home';
import Services from './pages/Services';
//componentes
import Navbar from './components/Navbar';
import Footer from './components/Footer/Footer';
import SignUp from './components/GetInTouch';
import Login from './components/Login'
import { useState } from "react";
import { CssBaseline } from "@mui/material";
import {Navigate, useLocation } from "react-router-dom";
import useNavigation from 'react-router-dom';



function App() {
  const [auth, setAuth] = useState(false);
  return (
    <>
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route index element={<Home />} />
          <Route path='/Home' element={<Home />} />
          <Route path='/services' element={<Services />} />
          <Route path='/signup' element={<SignUp />} />
          <Route path="/login" element={<Login />} />          
        </Routes>
      </BrowserRouter>
      <Footer />
    </>
  );
}

export default App;