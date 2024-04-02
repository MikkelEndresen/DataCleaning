import React, { useState } from 'react';
import Dropdown from './Dropdown';

const SelectDtypeComponent = () => {
  const [selectedOptions, setSelectedOptions] = useState({
    dropdown1: '',
    dropdown2: '',
    dropdown3: ''
  });

  const handleSubmit = (selectedOption, dropdownName) => {
    setSelectedOptions({
      ...selectedOptions,
      [dropdownName]: selectedOption
    });
  };

  const handleFinalSubmit = () => {
    console.log(selectedOptions);
  };

  return (
    <div>
      <h1>Dropdowns</h1>
      <Dropdown
        options={['Option 1', 'Option 2', 'Option 3']}
        onSubmit={(selectedOption) => handleSubmit(selectedOption, 'dropdown1')}
      />
      <Dropdown
        options={['Option A', 'Option B', 'Option C']}
        onSubmit={(selectedOption) => handleSubmit(selectedOption, 'dropdown2')}
      />
      <Dropdown
        options={['Apple', 'Banana', 'Orange']}
        onSubmit={(selectedOption) => handleSubmit(selectedOption, 'dropdown3')}
      />
      <button onClick={handleFinalSubmit}>Submit All</button>
    </div>
  );
};

export default SelectDtypeComponent;
