import os
import google.generativeai as genai
from IPython.display import Markdown
import textwrap
from .api_keys import GOOGLE_API_KEY

# run: 'gcloud auth application-default login', to login
# You are in the llm-rag project
# Service id: figure12-34@llm-rag-415122.iam.gserviceaccount.com

class dataTypeLLM:
    
    def __init__(self):
        self.setup_api()
        self.model = genai.GenerativeModel('gemini-pro')
        

    def to_markdown(self, text):
        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

    def setup_api(self):
        # Check if the environment variable exists
        if 'GOOGLE_API_KEY' in os.environ:
            print(f"The environment variable GOOGLE_API_KEY exists with value: {os.environ['GOOGLE_API_KEY']}")
        else:
            os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY
            print(f"Succesfully set the GOOGLE_API_KEY")

        genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

    def prompt(self, input):
        response = self.model.generate_content(input)
        return response.parts
    

def llm_to_dtype(head):
    queryDataTypeTemplate = f"""
        Context: You are an expert Data Scientist that has been tasked with selecting the appropriate pandas
        dtypes.

        The pandas dtypes you can choose from are: [object, int64, int32, int6, int8, float64, float32, 
        bool, datetime64, timedelta, category, complex]

    
        You will take the first three rows of a pandas dataframe (data), inlcuding the headers, and determine the
        appropriate dtype that I should use. 
        Please refer from using object as a dtype if possible.
        timedelta: Timedeltas are differences in times, expressed in difference units, e.g. days, hours, minutes, seconds. They can be both positive and negative.
        Please only return the dtypes and NOTHING ELSE 
        Return what you suggest in the same order as they were read such that they correspond to the correct dataframe column. Refer to the example output.

        Data: [{head}]

        Example input:[ Data: [      Name  Birthdate Score Grade TimeAlive
                                0    Alice  1/01/1990    90     A    45 days
                                1      Bob  2/02/1991    75     B    30 days
                                2  Charlie  3/03/1992    85     A    11 hours]]
        
        Example Output: [object, datetime64, int32, category, timedelta]
    """

    print(queryDataTypeTemplate)

    gem = dataTypeLLM()

    response = gem.prompt(queryDataTypeTemplate)
    print(response)

    print(80*'-')
    def format_result(text):
        """
        Format text response from LLM into array of strings

        Return:
            - Array of strings
        """
        print(f'this is the text: {text}')
        text = str(text).replace('[text: "[', '').replace(']"\n]', '')
        text = text.replace(',', '')
        entries = text.split()
        print(entries) # TODO: Remove
        print(len(entries)) # TODO: Remove

        return entries

    dtypes = format_result(response)
    return dtypes