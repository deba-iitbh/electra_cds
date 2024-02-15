// ProductForm.js
import React, { useState } from 'react';

const DeleteProduct = ({ onSubmit }) => {
  const [productId, setProductId] = useState('');
  const [productName, setProductName] = useState('');
  const [productPrice, setProductPrice] = useState('');

  const handleAddProduct = async () => {
    const updatedProduct = {
      id: productId,
      name: productName,
      price: productPrice,
    };

    try {
      await fetch('/api/products', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(updatedProduct),
      });
      onSubmit();
      setProductId('');
      setProductName('');
      setProductPrice('');
    } catch (error) {
      console.error('Error adding product:', error);
    }
  };

  const handleDeleteProduct = async () => {
    try {
      await fetch(`/api/products/${productId}`, {
        method: 'DELETE',
      });
      onSubmit();
      setProductId('');
      setProductName('');
      setProductPrice('');
    } catch (error) {
      console.error('Error deleting product:', error);
    }
  };

  return (
    <div>
      <h2>Product Form</h2>
      <div>
        <label>Product ID:</label>
        <input
          type="text"
          value={productId}
          onChange={(e) => setProductId(e.target.value)}
        />
      </div>
      <div>
        <label>Product Name:</label>
        <input
          type="text"
          value={productName}
          onChange={(e) => setProductName(e.target.value)}
        />
      </div>
      <div>
        <label>Product Price:</label>
        <input
          type="text"
          value={productPrice}
          onChange={(e) => setProductPrice(e.target.value)}
        />
      </div>
      <button onClick={handleDeleteProduct}>Delete Product</button>
    </div>
  );
};

export default DeleteProduct;
