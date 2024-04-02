import React, { useState, useEffect } from 'react';

const Dropdown = ({options, onSubmit}) => {
    const [selectedOption, setSelectedOption] = useState('');

    const handleChange = (e) => {
        setSelectedOption(e.target.value);
    };

    const handleSubmit = () => {
        onSubmit(selectedOption);
        setSelectedOption('');
    };

    return (
        <div>
          <select value={selectedOption} onChange={handleChange}>
            <option value="">Select an option</option>
            {options.map((option, index) => (
              <option key={index} value={option}>
                {option}
              </option>
            ))}
          </select>
          <button onClick={handleSubmit}>Submit</button>
        </div>
      );
};

export default Dropdown;