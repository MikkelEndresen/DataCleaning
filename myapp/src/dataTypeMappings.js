
// Pandas to user-friendly datatypes
const dataTypeMappings = {
    'Integer': ['Int64', 'Int32', 'Int16', 'Int8'],
    'Decimal': ['float64', 'float32'],
    'Text': ['object'],
    'True/False': ['bool'],
    'Date': ['datetime64', 'datetime64[ns]'],
    'Time Period': ['timedelta'],
    'Complex numbers': ['complex128'],
    'Category': ['category'],
};

// Mapping user-friendly to pandas
export const mapUserToData = (dataType) => {
    const mappedValues = dataTypeMappings[dataType];
    return mappedValues ? mappedValues[0] : dataType; // returns first in list
};

// Mapping pandas to user-friendly
export const mapDataToUser = (input) => {
    input = input.trim();
    for (const key in dataTypeMappings) {
        if (dataTypeMappings[key].includes(input)) {
            return key;
        }
    }
    return "Unknown"; // Return "Unknown" if input value is not found in any mapping
};

