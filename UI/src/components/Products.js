import React from 'react';
import ProductCart from './Product';
import Pagination from './Pagination';
import SearchNavbar from './SearchNavbar';
import { Box } from '@mui/material';
import ProductPage from './Product';
import CartPage from './Cart';



const Products = () => { 
  return (
    <div>
    <div>
      <SearchNavbar />
    </div>
    <Box>
      <ProductPage /> 
    </Box>
    <CartPage />
    </div>
    
  );
};

export default Products;
