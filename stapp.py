import streamlit as st
from keywads import SourceFileTransformer, KeywordAnalyzer
import os
import shutil

# Set a fixed output file path
output_path = 'output'

# Function to ensure the output directory exists
def ensure_output_path_exists():
    if not os.path.exists(output_path):
        os.makedirs(output_path)

# Function to delete all files in the output directory
def cleanup_output_directory():
    for filename in os.listdir(output_path):
        file_path = os.path.join(output_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            st.error(f'Failed to delete {file_path}. Reason: {e}')

# Function to check if the uploaded file is an Excel file
def is_excel_file(file_name):
    return file_name.endswith('.xlsx')

# Main app function
def main():
    st.title('Keyword Analysis Tool')

    if 'upload_completed' not in st.session_state:
        st.session_state['upload_completed'] = False

    if 'download_completed' not in st.session_state:
        st.session_state['download_completed'] = False

    # Instructions for the user about the file format
    st.markdown("""
        Please upload the **Excel (.xlsx)** version of the Keywords ideas spreadsheet downloaded from the Google Keyword Planner. 
        If you have a .csv file, please open it in Excel or a similar program and save it as a .xlsx file before uploading.
        """)

    # File uploader allows user to add their own file
    uploaded_file = st.file_uploader("Upload your input Excel file", type=['xlsx'])

    if uploaded_file is not None and not st.session_state['upload_completed']:
        if not is_excel_file(uploaded_file.name):
            st.error("Please upload an Excel file (.xlsx). If your file is in another format, convert it to .xlsx and try again.")
            return

        # Process the file
        try:
            st.info("Processing the uploaded file...")
            file_path = save_uploaded_file(uploaded_file)
            st.session_state['upload_completed'] = True
            
            transformer = SourceFileTransformer(source_file_path=file_path)
            transformer.load_and_transform_source()

            transformed_file_path = os.path.join(output_path, 'transformed_' + uploaded_file.name)
            transformer.save_transformed_file(output_path=transformed_file_path)

            analyzer = KeywordAnalyzer(file_path=transformed_file_path)
            analysis_output_file_name = os.path.join('Top_200_Keywords.xlsx')
            analyzer.run_analysis(output_file_name=analysis_output_file_name)
            downloadable_file = 'output\Top_200_Keywords.xlsx'

            # Let users download the output file
            try:
                with open(downloadable_file, "rb") as file:
                    btn = st.download_button(
                        label="Download analysis output",
                        data=file,
                        file_name='Top_200_Keywords.xlsx',
                        mime="application/vnd.ms-excel",
                        on_click=mark_download_complete
                    )
                st.success("Analysis complete. Please download the output file.")
            except IOError as e:
                st.error(f"Failed to open the output file for downloading: {e}")

        except Exception as e:
            st.error(f"An error occurred during processing: {e}")

    if st.session_state['download_completed']:
        cleanup_session_files()
        st.session_state['upload_completed'] = False
        st.session_state['download_completed'] = False
        st.info("Session reset. You can upload a new file.")

def mark_download_complete():
    st.session_state['download_completed'] = True

# Function to save uploaded file to a temporary path
def save_uploaded_file(uploaded_file):
    ensure_output_path_exists()
    temp_file_path = os.path.join(output_path, uploaded_file.name)
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return temp_file_path

# Function to clean up session files
def cleanup_session_files():
    cleanup_output_directory()

# Run the main function
if __name__ == "__main__":
    main()
