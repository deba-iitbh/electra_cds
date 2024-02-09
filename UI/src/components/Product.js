import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

const ProductPage = () => {
  const [products, setProducts] = useState([]);
  const [page, setPage] = useState(1);
  const [pageSize] = useState(10); // Number of products per page

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await fetch(`http://example.com/api/products?page=${page}&pageSize=${pageSize}`);
        if (!response.ok) {
          throw new Error('Failed to fetch products');
        }

        const data = await response.json();
        setProducts(data);
      } catch (error) {
        console.error('Error fetching products:', error.message);
      }
    };

    fetchProducts();
  }, [page, pageSize]);

  const addToCart = async (productId) => {
    try {
      const response = await fetch(`http://example.com/api/cart/add/${productId}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ productId }),
      });

      if (!response.ok) {
        throw new Error('Failed to add product to cart');
      }

      // Handle success
    } catch (error) {
      console.error('Error adding product to cart:', error.message);
    }
  };

  const removeFromCart = async (productId) => {
    try {
      const response = await fetch(`http://example.com/api/cart/remove/${productId}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ productId }),
      });

      if (!response.ok) {
        throw new Error('Failed to remove product from cart');
      }

      // Handle success
    } catch (error) {
      console.error('Error removing product from cart:', error.message);
    }
  };

  const handlePageChange = (newPage) => {
    setPage(newPage);
  };

  // Calculate the start and end index of products to be displayed on the current page
  const startIndex = (page - 1) * pageSize;
  const endIndex = Math.min(startIndex + pageSize, products.length);

  return (
    <div>
      <h1>Product Page</h1>
      <div style={{ display: 'flex', flexWrap: 'wrap' }}>
        {products.slice(startIndex, endIndex).map((product) => (
          <div key={product.id} style={{ border: '1px solid #ccc', padding: '10px', margin: '10px', width: '300px' }}>
            <h3>{product.name}</h3>
            <p>Description: {product.description}</p>
            <p>Price: ${product.price}</p>
            <p>Quantity: {product.quantity}</p>
            <button onClick={() => addToCart(product.id)}>+</button>
            <button onClick={() => removeFromCart(product.id)}>-</button>
          </div>
        ))}
      </div>
      <div>
        <button onClick={() => handlePageChange(page - 1)} disabled={page === 1}>Previous</button>
        <button onClick={() => handlePageChange(page + 1)}>Next</button>
      </div>
      <Link to="/cart">Go to Cart</Link>
    </div>
  );
};

export default ProductPage;
