**Document Analysis Streamlit App**  
This is a Streamlit-based app designed for analyzing and coding
structured documents. It supports extracting content from uploaded
files, structuring the document based on user-defined parameters, and
generating qualitative coding using OpenAI\'s GPT models.  
**Features**

1.  Upload and process files in PDF or DOCX formats.

<!-- -->

1.  Extract specific pages from the document.

<!-- -->

1.  Structure the extracted document for analysis.

<!-- -->

1.  Tag and theme management with user-defined inputs.

<!-- -->

1.  Generate qualitative coding using OpenAI GPT models.

<!-- -->

1.  Analyze structured data with visualizations (e.g., bar charts, pie
    charts).  
    **Prerequisites**

- Python 3.8 or higher

<!-- -->

- OpenAI Python package (ensure an active API key)  
  **Installation**  
  Step 1: Clone the Repository  
  Clone the repository to your local machine:  
  `bash`  
  Copy code  
  `git clone https://github.com/your-username/document-analysis-streamlit.git`  
  `cd document-analysis-streamlit`  
  **Step 2: Create a Virtual Environment**  
  Create and activate a virtual environment to isolate dependencies:  
  `bash`  
  Copy code  
  `python3 -m venv env`  
  `source env/bin/activate  # On Windows: env``\``Scripts``\``activate`  
  **Step 3: Install Dependencies**  
  Install the required Python packages using pip:  
  `bash`  
  Copy code  
  `pip install -r requirements.txt`  
  **Running the App**

1.  Place the required default file (e.g., `6.4 Teacher Guide.pdf`) in
    the specified path or modify the code to reflect the new default
    path.

<!-- -->

1.  Run the Streamlit app:  
    `bash`  
    Copy code  
    `streamlit run app.py`  
    **Usage Instructions**

<!-- -->

1.  Launch the app in your browser after running the above command.

<!-- -->

1.  Follow the steps in the app interface:

    - Upload a document or use the default file.

    <!-- -->

    - Extract pages from the document.

    <!-- -->

    - Structure the document using user-defined units, lessons, and
      themes.

    <!-- -->

    - Generate a codebook by entering research questions and leveraging
      OpenAI\'s API.

<!-- -->

1.  Enter your OpenAI API key in the provided input field if required.  
    **Troubleshooting**

<!-- -->

1.  Error with OpenAI API: Ensure you have sufficient quota and have
    entered a valid API key.

<!-- -->

1.  **File Path Issues**: Verify the path for the default file or
    uploaded files.

<!-- -->

1.  **Python Version**: Ensure you are running Python 3.8 or higher.

<!-- -->

1.  **Dependencies Not Installed**: Run
    `pip install -r requirements.txt` again in the virtual
    environment.  
    **Notes**

- Ensure you have a valid OpenAI API key before attempting to generate
  qualitative coding.

<!-- -->

- Modify `app.py` to update default file paths or change themes/tags.
