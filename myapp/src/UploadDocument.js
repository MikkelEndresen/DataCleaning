import React, { useState } from 'react';
//import axios from 'axios';


const FileUploadComponent = () => {
    console.log("Rendering FileUploadComponent");
  
    const [file, setFile] = useState(null);
  
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
          console.log("Upload response:", data);
        } catch (error) {
          console.error("Upload error:", error);
        }
      } else {
        console.log("No file selected for upload");
      }
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
      </>
    );
  };
  
export default FileUploadComponent;