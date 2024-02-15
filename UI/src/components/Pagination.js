import React, { useState } from 'react';

const Pagination = ({ data, itemsPerPage, renderComponent }) => {
  const [currentPage, setCurrentPage] = useState(1);

  const maxPage = Math.ceil(data.length / itemsPerPage);

  const nextPage = () => {
    setCurrentPage((prev) => (prev === maxPage ? prev : prev + 1));
  };

  const prevPage = () => {
    setCurrentPage((prev) => (prev === 1 ? prev : prev - 1));
  };

  const changePage = (page) => {
    setCurrentPage(page);
  };

  const getPaginatedData = () => {
    const startIndex = (currentPage - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;
    return data.slice(startIndex, endIndex);
  };

  return (
    <div>
      {renderComponent(getPaginatedData())}
      <div>
        <button onClick={prevPage} disabled={currentPage === 1}>
          Previous
        </button>
        {Array.from({ length: maxPage }, (_, i) => (
          <button key={i + 1} onClick={() => changePage(i + 1)}>
            {i + 1}
          </button>
        ))}
        <button onClick={nextPage} disabled={currentPage === maxPage}>
          Next
        </button>
      </div>
    </div>
  );
};

export default Pagination;
