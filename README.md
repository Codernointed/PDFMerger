﻿# PDF Merger App

This Streamlit app allows you to combine multiple PDF files into a single document.
(I personally used this to merge my HCI pdfs)
## Live Demo
Check out the live demo here: [PDF Merger App](https://mergemypdf.streamlit.app/)

## Features

- **Combine Multiple PDFs**: Upload and merge multiple PDF files into a single document.
- **Easy to Use**: Simple interface for uploading files and downloading the merged PDF.
- **Streamlit-Based**: Built with Streamlit for a user-friendly web interface.

## Requirements

- Python 3.x
- Streamlit
- PyPDF2
- Install pycyrptodome if there is an error in reading files

## Installation
Follow these steps to get the PDF Merger App up and running on your local machine:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Codernointed/PDFMerger.git
   cd PDFMerger
   ```

2. **Install Dependencies**:
   Ensure you have pip installed, then install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App**:
   Start the Streamlit app with the following command:
   ```bash
   streamlit run merge_pdfs.py
   ```
   This will open the app in your default web browser.

## Usage
- **Upload PDF Files**: Click on the file uploader to select and upload the PDF files you want to merge.
- **Merge PDFs**: After uploading, click the "Merge PDFs" button.
- **Download**: Once the merging is complete, download the combined PDF using the provided download button.

## Troubleshooting
- **Installation Issues**: Ensure all dependencies are correctly installed. If you encounter issues with file reading, try installing pycryptodome:
  ```bash
  pip install pycryptodome
  ```

- **Running the App**: If Streamlit fails to run, ensure you are using Python 3.x and that Streamlit is properly installed.

## Contributing
Contributions are welcome! If you have suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or feedback, you can reach out to botchweypaul0001@gmail.com.
Cheers!
