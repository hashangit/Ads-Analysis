# Keyword Analysis Tool
## https://gads-toolkit.streamlit.app/

This tool is designed to assist in analyzing keywords from Google Keyword Planner by processing Excel (.xlsx) files containing keyword data. It simplifies the analysis of keyword ideas, enabling users to easily identify the most valuable keywords for their SEO or SEM campaigns.

## Features

- **File Upload**: Users can upload Excel files (.xlsx) directly into the tool.
- **Data Transformation**: The tool transforms the uploaded Excel file to prepare the data for analysis.
- **Keyword Analysis**: Performs a comprehensive analysis of the transformed keyword data.
- **Downloadable Analysis**: Users can download the analysis results in an Excel file format.

## Installation

This tool is built using Streamlit and requires Python for execution. Ensure you have Python installed on your system before proceeding.

1. Clone or download this repository to your local machine.
2. Navigate to the directory containing the tool in your terminal.
3. Install the required Python packages by running:

```bash
pip install -r requirements.txt
```

## Usage

To use the tool, follow these steps:

1. Start the Streamlit application by running:

```bash
streamlit run your_script_name.py
```

Replace `your_script_name.py` with the actual name of the Python script.

2. Open your web browser and go to the address provided by Streamlit, typically `http://localhost:8501`.
3. Follow the on-screen instructions to upload your Excel (.xlsx) file containing keywords.
4. Wait for the tool to process your file and perform the keyword analysis.
5. Download the analysis output once it's ready.

## File Requirements

- The tool currently supports **Excel (.xlsx)** files only.
- Ensure your file contains the keyword data exported from Google Keyword Planner.

## Limitations

- File upload size is limited by Streamlit's configuration.
- The tool is optimized for English-language keyword data.

## Customization

You can customize the analysis parameters and output format by modifying the source code. Please refer to the source files for more detailed information on how the analysis is performed.

## Support

For issues, suggestions, or contributions, please open an issue on the GitHub repository page.

## License

This tool is open-source and available under the MIT license. See the LICENSE file for more details.
