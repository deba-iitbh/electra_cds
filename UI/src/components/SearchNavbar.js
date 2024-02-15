import React, { useState, useRef, useEffect } from 'react';
import { ListItemButton, TextField } from '@mui/material';
import { Link } from 'react-router-dom';
import { Button } from 'react-bootstrap';
import styled from '@emotion/styled';
import { motion } from "framer-motion";

export default function SearchNavbar() {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState(null);
  const pnameRef = useRef('');
  const [isCustomer, setIsCustomer] = useState(false); // State to track if user is a customer

  useEffect(() => {
    // Simulated function to determine if the user is a customer
    const checkUserRole = async () => {
      // Replace this with your actual logic to fetch user role
      // Simulated API call
      const response = await fetch("YOUR_USER_ROLE_API_ENDPOINT_HERE", {
        method: "GET",
        headers: {
          "Authorization": "Bearer YOUR_ACCESS_TOKEN_HERE", // Add your access token here
          "Content-Type": "application/json",
        },
      });
      const userData = await response.json();

      // Simulated check if user is a customer
      const isCustomerUser = userData.role === 'customer'; // Adjust this based on your actual user data structure

      setIsCustomer(isCustomerUser);
    };

    checkUserRole();
  }, []);

  const handleSearch = async (event) => {
    // Simulated search logic...
  };

  const CustomButton = styled(Button)({
    backgroundColor: '#CDAFE4',
    width: 100,
    height: 50,
    ml: 140,
    placeContent: 'center',
    position: 'absolute',
    left: 1050,
    bottom: 550,
  });
  
  const ListItemButton1 = styled(ListItemButton)({
    backgroundColor: '#CDAFE4',
    width: 80,
    height: 50,
    ml: 140,
    placeContent: 'center',
    position: 'absolute',
    left: 1200,
    bottom: 550,
  });

  const ListItemButton2 = styled(ListItemButton)({
    backgroundColor: '#CDAFE4',
    width: 80,
    height: 50,
    ml: 140,
    placeContent: 'center',
    position: 'absolute',
    left: 1300,
    bottom: 550,
  });

  const ListItemButton3 = styled(ListItemButton)({
    backgroundColor: '#CDAFE4',
    width: 80,
    height: 50,
    ml: 140,
    placeContent: 'center',
    position: 'absolute',
    left: 1400,
    bottom: 550,
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

  return (
    <div>
      <div style={{ backgroundColor: "#7F4988", height: 120 }}>
        <TextField
          sx={{ backgroundColor: '#CDAFE4', width: 800, mt: 6, ml: 18, mb: 10 }}
          required
          fullWidth
          id="pname"
          label="Product Name"
          name="pname"
          autoComplete="pname"
          inputRef={pnameRef}
        />

        <CustomButton onClick={handleSearch}>Search</CustomButton>
        {!isCustomer && (
          <ListItemButton1 component={Link} to={'/addproduct'}>Add Product</ListItemButton1>
        )}
        {!isCustomer && (
          <ListItemButton2 component={Link} to={'/deleteproduct'}>Delete Product</ListItemButton2>
        )}
        {!isCustomer && (
          <ListItemButton3 component={Link} to={'/modifyproduct'}>Modify Product</ListItemButton3>
        )}

        {searchResults && (
          <motion.div
            initial="initial"
            animate="animate"
            variants={fadeInUp}
            style={{ marginTop: 20, padding: 20, backgroundColor: '#fff' }}
          >
            <h2>Search Results</h2>
            <pre>{JSON.stringify(searchResults, null, 2)}</pre>
          </motion.div>
        )}
      </div>
    </div>
  );
}
