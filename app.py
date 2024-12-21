# Import necessary modules
import os
import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
import pandas as pd
import re  # Import the regular expressions module
import openai

# Set OpenAI API key
openai.api_key = "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"

# Helper functions
def extract_text_from_pdf(file):
    """Extract text from PDF file."""
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(file):
    """Extract text from Word document."""
    doc = Document(file)
    text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    return text

def validate_file(uploaded_file):
    """Validate uploaded file format."""
    if uploaded_file is None:
        st.error("Please upload a file.")
        return None
    if not uploaded_file.name.lower().endswith((".pdf", ".docx", ".txt", ".csv", ".xlsx")):
        st.error("Unsupported file format. Please upload a PDF, Word, text, CSV, or Excel file.")
        return None
    return uploaded_file

# Streamlit app
st.title("Document Analysis Tool")

# Step 1: File Upload
st.header("Step 1: Upload Document")

# Preload default file
default_file_path = "/Users/sayuj/Downloads/phd/PHD Resources/Course Material/Y1S2/QE AB/QE Project/US CMs/IM/6.4 Teacher Guide.pdf"

uploaded_file = st.file_uploader(
    "Upload a document (PDF, DOCX, etc.)",
    type=["pdf", "docx", "txt", "csv", "xlsx"],
    help="Supported formats: PDF, DOCX, TXT, CSV, XLSX"
)

if not uploaded_file:
    # Provide default file if no file is uploaded
    st.warning("No file uploaded. Using the default file.")
    uploaded_file = default_file_path

# Validate the file
def validate_file(file):
    if file and isinstance(file, str) and not os.path.isfile(file):
        st.error("Invalid file path or format.")
        return None
    return file

file = validate_file(uploaded_file)

if file:
    st.success(f"File loaded: {os.path.basename(file)}")

# Step 2: Document Category Selection
st.header("Step 2: Select Document Category")

# Default selection for category
category = st.selectbox(
    "Select the document category:",
    ["Curriculum Materials", "Transcripts", "Administrative Documents", "Field Notes"],
    index=0  # Default to "Curriculum Materials"
)

# Step 3: Sub-category Selection
st.header("Step 3: Select Sub-Category")

if category == "Curriculum Materials":
    doc_type = st.selectbox(
        "Select the type of curriculum material:",
        ["Textbooks", "Lesson Plans", "Teacher Guides", "Workbooks", "Custom"],
        index=2  # Default to "Teacher Guides"
    )
elif category == "Transcripts":
    doc_type = st.selectbox(
        "Select the type of transcript:",
        ["Interview Transcripts", "Meeting Transcripts", "Classroom Transcripts", "Custom"]
    )
elif category == "Administrative Documents":
    doc_type = st.text_input("Enter the document type (Custom):")
elif category == "Field Notes":
    doc_type = st.text_input("Enter the document type (Custom):")

    # Step 4: Structure your document
    if st.checkbox("Would you like to structure your document?"):
        st.write(f"Suggested structure for {category}: {doc_type}")
        if category == "Curriculum Materials":
            structure = {
                "Textbooks": ["Lines", "Unit", "Lesson", "Sections", "Subsections", "Page Number", "Tags", "Themes"],
                "Lesson Plans": ["Lines", "Unit", "Lesson", "Objectives", "Materials", "Activities", "Assessment", "Reflection"],
                "Teacher Guides": ["Lines", "Unit", "Lesson", "Sections", "Subsections", "Page Number", "Tags", "Themes"],
                "Workbooks": ["Instructions", "Examples", "Problems", "Answer Key"],
                "Custom": ["Custom structure"]
            }
            st.write(structure.get(doc_type, "Custom structure"))

    # Step 5: Add tags and themes
        st.header("Step 5: Structure Your Document")
        st.markdown("### Suggested Structure for Curriculum Materials: Teacher Guides")

# Default structure for Teacher Guides
default_structure = {
    "Column Name": ["Lines", "Unit", "Lesson", "Sections", "Subsections", "Page Number", "Tags", "Themes"]
}

# Convert to DataFrame for editable table
structure_df = pd.DataFrame(default_structure)

# Editable Table for structure
edited_structure = st.data_editor(
    structure_df, use_container_width=True, num_rows="dynamic"
)

st.write("Modified Structure:")
st.write(edited_structure)

# Step 6: Theme and Tags Table
st.header("Step 6: Add Tags and Themes")
st.markdown("### Organize Tags by Themes")

# Default themes and associated tags (example)
default_data = {
    "Theme": ["Learning Goals", "Teacher Role", "Assessment", "Student"],
    "Tags": ["Plan, Facilitate, Guide", "Teach, Mentor, Support", "Evaluate, Grade, Feedback", "Share, Discuss"]
}

# Convert to DataFrame for editing
themes_tags_df = pd.DataFrame(default_data)

# Editable Table for Themes and Tags
edited_themes_tags = st.data_editor(
    themes_tags_df, use_container_width=True, num_rows="dynamic"
)

# Display the modified themes and tags
st.write("Modified Themes and Tags:")
st.write(edited_themes_tags)

# Save the modified DataFrame to session state for later use
st.session_state["themes_tags_df"] = edited_themes_tags


import streamlit as st
from PyPDF2 import PdfReader
import os

# Step 7: Extract pages
st.header("Step 7: Extract Pages")

# Default path to the preloaded document
default_file_path = "/Users/sayuj/Downloads/phd/PHD Resources/Course Material/Y1S2/QE AB/QE Project/US CMs/IM/6.4 Teacher Guide.pdf"

# Check if the file exists
if os.path.exists(default_file_path):
    st.write(f"Default file loaded: {os.path.basename(default_file_path)}")
    default_file_loaded = True
else:
    st.error(f"Default file not found at: {default_file_path}")
    default_file_loaded = False

# User inputs for page range
start_page = st.number_input("Enter the start page:", min_value=1, step=1, value=198)
end_page = st.number_input("Enter the end page:", min_value=start_page, step=1, value=235)

# Function to extract text from a PDF
def extract_text_from_pdf(file_path, start_page, end_page):
    """Extract text from a PDF file within a given page range."""
    reader = PdfReader(file_path)
    text = ""
    for page_num in range(start_page - 1, end_page):  # Convert to zero-based index
        if page_num < len(reader.pages):
            text += reader.pages[page_num].extract_text() + "\n"
        else:
            st.warning(f"Page {page_num + 1} does not exist in the document.")
    return text

# Button to trigger extraction
if st.button("Extract Pages"):
    if default_file_loaded:
        st.write("Extracting lines from the selected pages...")
        full_text = extract_text_from_pdf(default_file_path, start_page, end_page)
        if full_text:
            # Process text into structured lines
            raw_lines = full_text.splitlines()
            processed_lines = []
            current_line = ""

            for i, line in enumerate(raw_lines):
                line = line.strip()

                # Skip lines starting with a., b., c., d., e.
                if line.startswith(("a.", "b.", "c.", "d.", "e.")):
                    continue

                # Combine lines based on lowercase starts
                if current_line:
                    if (
                        line and
                        not line[0].isupper() and  # If the next line starts with a lowercase letter
                        not line.startswith("a.")  # Ensure it does not start with "a.", "b.", etc.
                    ):
                        current_line += " " + line  # Concatenate to the previous line
                    else:
                        processed_lines.append(current_line)  # Save the completed line
                        current_line = line  # Start a new line
                else:
                    current_line = line

            # Add the last line if it exists
            if current_line:
                processed_lines.append(current_line)

            # Further split sentences using punctuation
            final_lines = []
            for line in processed_lines:
                # Split based on sentence-ending punctuation followed by a space or end of line
                import re
                sentences = re.split(r'(?<=[.!?])\s+', line)
                final_lines.extend(sentences)

            # Save the extracted lines in session state
            st.session_state["lines"] = final_lines

            # Display the first 50 lines as a preview
            st.write("Extracted Lines Preview:")
            for i, line in enumerate(final_lines[:50], start=1):
                st.write(f"{i}. {line}")
        else:
            st.warning("No text extracted. Please check the selected file and page range.")
    else:
        st.error("No default file is loaded. Please provide a valid file.")

# Step 8: Structure the Document
st.header("Step 8: Structure the Document")

# Ask user to input Unit and Lesson
unit = st.text_input("Enter the Unit:")
lesson = st.text_input("Enter the Lesson:")

if st.button("Structure Document"):
    # Check if lines are available in session state
    if "lines" not in st.session_state or not st.session_state["lines"]:
        st.error("Please extract lines before structuring the document.")
    else:
        st.write("Structuring the document based on the user-defined structure...")

        # Load extracted lines
        lines = st.session_state["lines"]

        # Load themes and tags DataFrame from session state
        if "themes_tags_df" not in st.session_state or st.session_state["themes_tags_df"].empty:
            st.error("Themes and tags data not available. Please complete Step 6 before proceeding.")
        else:
            themes_tags_df = st.session_state["themes_tags_df"]

        # Prepare structured data
        structured_data = []
        current_section = ""  # Track current section
        current_subsection = ""  # Track current subsection

        for idx, line in enumerate(lines):
            structured_row = {
                "Lines": line,
                "Unit": unit,
                "Lesson": lesson,
                "Sections": current_section,
                "Subsections": current_subsection,
                "Tags": "",  # Placeholder for Tags
                "Themes": ""  # Placeholder for Themes
            }

            # Check if line is a heading (all uppercase)
            if line.isupper():
                current_section = line
                structured_row["Sections"] = current_section
                current_subsection = ""  # Reset subsection on new section

            # Check if line is a subheading (title case)
            elif line.istitle():
                current_subsection = line
                structured_row["Subsections"] = current_subsection

            # Convert line to lowercase for case-insensitive matching
            line_lower = line.lower()

            # Detect tags in the line
            detected_tags = []
            for _, row in themes_tags_df.iterrows():
                theme_tags = row["Tags"].split(",")  # Split tags by commas
                theme_tags = [tag.strip().lower() for tag in theme_tags]  # Clean tags
                for tag in theme_tags:
                    if pd.notna(tag) and re.search(rf'\b{tag}\b', line_lower):  # Match whole words
                        detected_tags.append(tag)

            # Add unique tags to the row
            structured_row["Tags"] = ", ".join(set(detected_tags))  # Ensure unique tags

            # Detect themes based on detected tags
            detected_themes = []
            for _, row in themes_tags_df.iterrows():
                theme = row["Theme"]
                theme_tags = row["Tags"].split(",")  # Split tags by commas
                theme_tags = [tag.strip().lower() for tag in theme_tags]  # Clean tags
                if any(tag in detected_tags for tag in theme_tags):
                    detected_themes.append(theme)

            # Add unique themes to the row
            structured_row["Themes"] = ", ".join(set(detected_themes))  # Ensure unique themes

            # Append structured row to data
            structured_data.append(structured_row)

        # Convert structured data to DataFrame
        df_structured = pd.DataFrame(structured_data)

        # Save structured data to session state
        st.session_state["structured_document"] = df_structured

        # Display the first 50 lines as preview
        st.subheader("Structured Document Preview (First 50 Lines)")
        st.dataframe(df_structured.head(50))

        # Allow the user to download the structured document
        st.download_button(
            label="Download Structured Document as CSV",
            data=df_structured.to_csv(index=False),
            file_name="structured_document.csv",
            mime="text/csv"
        )

        st.success("Document structured successfully!")

# Step 9: Analyze Document
st.header("Step 9: Analyze Document")

# Check if the structured document is available in session state
if "structured_document" in st.session_state and not st.session_state["structured_document"].empty:
    # Load the structured document from session state
    df_structured = st.session_state["structured_document"]

    # Display preview of structured document
    st.subheader("Preview Structured Document (First 50 Rows)")
    st.dataframe(df_structured.head(50))

    # Ask user to confirm the structured document
    if st.checkbox("Confirm Structured Document"):
        # Ask if user wants to do preliminary analysis
        if st.checkbox("Would you like to analyze the structured document?"):
            if st.button("Analyze Document"):
                st.write("Analysis in progress...")

                # Analysis Logic
                # Frequency chart of Tags
                st.subheader("Frequency of Tags")
                if "Tags" in df_structured.columns:
                    tags = (
                        df_structured["Tags"]
                        .str.split(", ")
                        .explode()  # Split and expand tags
                        .value_counts()
                    )
                    st.bar_chart(tags)
                else:
                    st.warning("No Tags column found in the structured document.")

                # Frequency chart of Themes
                st.subheader("Frequency of Themes")
                if "Themes" in df_structured.columns:
                    themes = (
                        df_structured["Themes"]
                        .str.split(", ")
                        .explode()  # Split and expand themes
                        .value_counts()
                    )
                    st.bar_chart(themes)
                else:
                    st.warning("No Themes column found in the structured document.")

                # Pie chart for Themes Distribution
                st.subheader("Distribution of Themes")
                if "Themes" in df_structured.columns:
                    import matplotlib.pyplot as plt

                    themes_pie = (
                        df_structured["Themes"]
                        .str.split(", ")
                        .explode()  # Split and expand themes
                        .value_counts()
                    )
                    # Create thread-safe Matplotlib figure
                    fig, ax = plt.subplots(figsize=(6, 6))
                    themes_pie.plot.pie(
                        autopct='%1.1f%%',
                        ax=ax,
                        legend=False,
                        title="Theme Distribution"
                    )
                    st.pyplot(fig)
                else:
                    st.warning("No Themes column found for pie chart.")

                st.success("Analysis complete!")
else:
    st.warning("Please structure the document before performing analysis.")

# Step 10: Generate Coding
st.header("Step 10: Generate Coding")

# Add API key input
if "openai_api_key" not in st.session_state:
    st.session_state["openai_api_key"] = ""

st.session_state["openai_api_key"] = st.text_input(
    "Enter your OpenAI API Key (required for generating coding):",
    value=st.session_state["openai_api_key"],
    type="password"
)

if st.session_state["openai_api_key"]:
    openai.api_key = st.session_state["openai_api_key"]

    if "structured_document" in st.session_state and not st.session_state["structured_document"].empty:
        df_structured = st.session_state["structured_document"]

        if st.checkbox("Confirm Structured Document for Coding"):
            if st.button("Generate Coding"):
                try:
                    st.write("Generating coding based on research questions...")

                    # Prepare the content to be sent for coding
                    structured_text = df_structured.to_csv(index=False)
                    research_questions = st.text_area(
                        "Enter research questions or context for coding:",
                        "What are the main themes in this document?"
                    )

                    # Generate the prompt
                    prompt = f"""You are an expert in qualitative data analysis. Based on the following structured document, generate a codebook for qualitative analysis:
                    Research Questions: {research_questions}

                    Document:
                    {structured_text}"""

                    # Call OpenAI API
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are an expert in qualitative data analysis."},
                            {"role": "user", "content": prompt}
                        ]
                    )

                    # Display the generated coding
                    generated_codebook = response["choices"][0]["message"]["content"]
                    st.subheader("Generated Codebook")
                    st.text(generated_codebook)

                    # Save the codebook in session state for further processing or download
                    st.session_state["generated_codebook"] = generated_codebook

                    # Provide download option
                    st.download_button(
                        label="Download Codebook as Text File",
                        data=generated_codebook,
                        file_name="generated_codebook.txt",
                        mime="text/plain"
                    )

                except openai.error.OpenAIError as e:
                    st.error(f"Error generating coding: {str(e)}")
else:
    st.warning("Please structure the document before generating coding.")

    # Step 9: Download results
    if st.button("Download Results"):
        st.write("Preparing downloadable file...")
        df = pd.DataFrame(lines, columns=["Extracted Lines"])
        csv = df.to_csv(index=False)
        st.download_button(label="Download CSV", data=csv, file_name="extracted_lines.csv", mime="text/csv")
