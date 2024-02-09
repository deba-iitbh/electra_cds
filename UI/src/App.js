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
import Products from './components/Products';
import AddProduct from './components/AddProduct';
import DeleteProduct from './components/DeleteProduct';
import ModifyProduct from './components/ModifyProduct';



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
          <Route path='/products' element={<Products />} />
          <Route path='/signup' element={<SignUp />} />
          <Route path="/login" element={<Login />} />          
          <Route path="/addproduct" element={<AddProduct />} />          
          <Route path="/deleteproduct" element={<DeleteProduct />} />          
          <Route path="/modifyproduct" element={<ModifyProduct />} />          
        </Routes>
      </BrowserRouter>
      <Footer />
    </>
  );
}

export default App;