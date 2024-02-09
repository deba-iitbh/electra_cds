// ProductForm.js
import { TextField } from '@mui/material';
import React, { useRef} from 'react';

const AddProduct = ({ onSubmit }) => {
  const productName = useRef('') 
  const productDesc = useRef('') 
  const productPrice = useRef('')
  const productQty = useRef('')
  
  const handleAddProduct = async () => {
    const addProduct = {
    
      name: productName.current.value,
      description: productDesc.current.value,
      price: parseFloat(productPrice.current.value),
      stock_quantity: parseInt(productQty.current.value),
    };
    console.log(addProduct)

    try {
      const response = await fetch('http://127.0.0.1:5000/api/v1/products/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(addProduct),
      });
      
      const result = await response.json();
    
      if (response.ok) {

      productName.current.value ='';
      productDesc.current.value ='';
      productPrice.current.value ='';
      productQty.current.value ='';
      }

    } catch (error) {
      console.error('Error adding product:', error);
    }
  };

  return (
    <div>
      <h2>Product Form</h2>
      <div>
        <label>Product Name:</label>
        <TextField
          type="text"
          inputRef={productName}
        />
      </div>
      <div>
        <label>Product Description:</label>
        <TextField
          type="text"
          inputRef={productDesc}
        />
      </div>
      <div>
        <label>Product Price:</label>
        <TextField
          type="text"
          inputRef={productPrice}
        />
      </div>
      <div>
        <label>Product Quantity:</label>
        <TextField
          type="text"
          inputRef={productQty}
        />
      </div>
      <button onClick={handleAddProduct}>Add Product</button>
    </div>
  );
};

export default AddProduct;
