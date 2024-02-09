import React, { useState, useEffect } from 'react';
import { Card, CardContent, Typography } from '@mui/material';

const CartPage = () => {
  const [cartProducts, setCartProducts] = useState([]);
  const [totalPrice, setTotalPrice] = useState(0);

  useEffect(() => {
    // Fetch cart products from server
    const fetchCartProducts = async () => {
      try {
        const response = await fetch("YOUR_CART_PRODUCTS_ENDPOINT_HERE");
        if (!response.ok) {
          throw new Error('Failed to fetch cart products');
        }
        const data = await response.json();
        setCartProducts(data.products);
        calculateTotalPrice(data.products);
      } catch (error) {
        console.error('Error fetching cart products:', error);
      }
    };

    fetchCartProducts();
  }, []);

  const calculateTotalPrice = (products) => {
    let total = 0;
    products.forEach(product => {
      total += product.price * product.quantity;
    });
    setTotalPrice(total);
  };

  return (
    <div>
      <Typography variant="h4" gutterBottom>
        Cart
      </Typography>
      {cartProducts.map(product => (
        <Card key={product.id} style={{ marginBottom: '20px' }}>
          <CardContent>
            <Typography variant="h5">{product.name}</Typography>
            <Typography variant="body1">Price: ${product.price}</Typography>
            <Typography variant="body1">Quantity: {product.quantity}</Typography>
          </CardContent>
        </Card>
      ))}
      <Typography variant="h6" style={{ marginTop: '20px' }}>
        Total Price: ${totalPrice}
      </Typography>
    </div>
  );
};

export default CartPage;
