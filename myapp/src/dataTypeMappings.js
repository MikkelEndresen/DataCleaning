
// Pandas to user-friendly datatypes
const dataTypeMappings = {
    'Integer': ['int64', 'int32', 'int16', 'int8'],
    'Decimal': ['float64', 'float32'],
    'Text': ['object'],
    'True/False': ['bool'],
    'Date': ['datetime64', 'datetime64[ns]'],
    'Time Period': ['timedelta'],
    'Complex numbers': ['complex'],
    'Category': ['category'],
};

// Mapping user-friendly to pandas
export const mapUserToData = (dataType) => {
    const mappedValues = dataTypeMappings[dataType];
    return mappedValues ? mappedValues[0] : dataType; // returns first in list
};

// Mapping pandas to user-friendly
export const mapDataToUser = (dataType) => {
    for (const key in dataTypeMappings) {
        console.log(key)
        console.log(dataType)
        if (Object.prototype.hasOwnProperty.call(dataTypeMappings, key)) {
            if (dataTypeMappings[key].includes(dataType)) {
                return key;
            }
        }
    }
    return dataType; // Return the original data type if no mapping is found
};

