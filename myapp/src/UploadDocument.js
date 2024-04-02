import React, { useState } from 'react';
//import axios from 'axios';


const FileUploadComponent = () => {
    console.log("Rendering FileUploadComponent");
  
    const [file, setFile] = useState(null);
    const [csvData, setCsvData] = useState(null); 
    const [dropdownValues, setDropdownValues] = useState([]);
    const [showDropdowns, setShowDropdowns] = useState(false);
    const [updatedCsv, setShowUpdatedCsv] = useState(false);

    const yourDropdownOptions = [
        "Select Option",
        "int",
        "float",
        "category",
        "datetime64",
        "bool",
        "complex",
        "timedelta",
        "object",
    ]

    const handleFileChange = (e) => {
      console.log("File change event:", e.target.files);
      if (e.target.files) {
        setFile(e.target.files[0]);
      }
    };
  
    const handleUpload = async () => {
      console.log("Uploading file...");
      if (file) {
        const formData = new FormData();
        formData.append("file", file);
  
        try {
          const result = await fetch("http://localhost:8000/api/upload-document/", {
            method: "POST",
            body: formData,
          });
          const data = await result.json();
          setCsvData(data); //
          setShowDropdowns(true);
          console.log("Upload response:", data);
        } catch (error) {
          console.error("Upload error:", error);
        }
      } else {
        console.log("No file selected for upload");
      }
    };

    const handleDtype = async () => {
        console.log("Changing dtypes");
        try {
            const result = await fetch("http://localhost:8000/api/select-dtype/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    'dtypes': dropdownValues,  // No need to stringify here
                    'file_path': csvData.file_path,  // No need to stringify here
                })
            });
        const data = await Response.json();
        setCsvData(data);
        setShowUpdatedCsv(true);
        console.log("Response from backend:", data);
        } catch (error) {
            console.error("Error submitting dropdown values:", error);
        }
    };


    const handleDropdownChange = (index, event) => {
        const updatedDropdownValues = [...dropdownValues];
        updatedDropdownValues[index] = event.target.value;
        setDropdownValues(updatedDropdownValues);
    };

    return (
      <>
        <div>
          <label htmlFor="file" className="sr-only">
            Choose a file
          </label>
          <input id="file" type="file" onChange={handleFileChange} />
        </div>
        {file && (
          <section>
            File details:
            <ul>
              <li>Name: {file.name}</li>
              <li>Type: {file.type}</li>
              <li>Size: {file.size} bytes</li>
            </ul>
          </section>
        )}
  
        {file && <button onClick={handleUpload}>Upload a file</button>}

        {csvData && ( 
        <div>
          <h2>CSV Data:</h2>
          <pre>{csvData.dtypes}</pre>
          <pre>{csvData.data}</pre>
        </div>
      )}
      <div>
        {showDropdowns && <h2>Change Dtypes</h2>}
        {showDropdowns && <button onClick={handleDtype}>Submit Dtype</button>}

        {showDropdowns && Array.from(Array(csvData.dtypes.length).keys()).map((index) => (
            <select key={index} value={dropdownValues[index] || ''} onChange={(event) => handleDropdownChange(index, event)}>
                {yourDropdownOptions.map((option, optionIndex) => (
                    <option key={optionIndex} value={option}>
                        {option}
                    </option>
                ))}
            </select>
        ))}

        <div> 
            {updatedCsv && (
                <div>
                <h2>CSV Data:</h2>
                <pre>{csvData.dtypes}</pre>
                <pre>{csvData.data}</pre>
              </div>
            )}

        </div>
        </div>
      </>
    );
  };

export default FileUploadComponent;