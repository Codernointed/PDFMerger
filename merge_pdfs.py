from PyPDF2 import PdfMerger
import streamlit as st
import io


st.set_page_config(page_title='PDF Merger App', page_icon=':page_facing_up:')

st.title('📄 PDF Merger App')
st.markdown("""
Combine multiple PDF files into a single document with ease. Simply Upload the PDFs you wish to merge, and then click the 'Download Merged PDF' button to get your combined document. Its not Perfect though so feel free to make it better.
""")


uploaded_files = st.file_uploader(
    'Choose PDF files to upload',
    type='pdf',
    accept_multiple_files=True,
    label_visibility='collapsed'
)


if uploaded_files:
    if len(uploaded_files) == 1:
        st.warning('Please upload more than one PDF file to merge.')
    else:
        st.info('All files uploaded. Click the button below to merge and download your combined PDF.')
        
        
        if st.button('Merge PDFs'):
            with st.spinner('Merging PDFs...'):
                merger = PdfMerger()
                for pdf in uploaded_files:
                    merger.append(io.BytesIO(pdf.read()))

                with io.BytesIO() as output_pdf:
                    merger.write(output_pdf)
                    output_pdf.seek(0)
                    st.download_button(
                        label='Download Merged PDF',
                        data=output_pdf.getvalue(),
                        file_name='merged.pdf',
                        mime='application/pdf',
                    )
                # merger.close()


with st.expander("About This App"):
    st.markdown("""
    **Developer**: Paul Botchwey  
    **Purpose**: This tool was created to simplify document management and enhance your productivity.  
    **Open Source**: Feel free to contribute, suggest improvements, or provide feedback. Your contributions are highly valued!
    **License**: MIT License - [Learn more](https://opensource.org/licenses/MIT)
    """)


st.markdown("""
<style>
    .css-16huue1 { background-color: #f0f0f5; }
    /* Button styling */
    .stButton>button {
        background-color: #007bff;
        color: white; /* Text color */
        border: none; 
        border-radius: 8px; /* Rounded corners */
        padding: 12px 24px; /* Padding for size */
        font-size: 16px; /* Font size */
        cursor: pointer; /* Pointer cursor on hover */
        transition: background-color 0.3s ease, transform 0.2s ease; /* Smooth transition */
    }
    .stButton>button:hover {
        background-color: #0056b3; 
        transform: scale(1.01);
        color: white; /* Text color */  
            
    }
    /* Button focus effect */
    .stButton>button:focus {
        outline: none; 
    }
    .css-1e4osb2 { border-radius: 10px; padding: 10px; }
    .css-1e4osb2 img { border-radius: 10px; }
    .css-1vj4b3k { font-size: 1.2em; }
    .css-1vk09h6 { color: #007bff; }
    .css-1g4y3k7 { text-align: center; }
</style>
""", unsafe_allow_html=True)



#   pdf_paths = ['TestFiles/Chapter 1 HCI.pdf', 'TestFiles/Chapter 2 - HCI.pdf', 'TestFiles/Chapter 3.pdf', 'TestFiles/Chapter 4.pdf', 'TestFiles/Chapter 5.pdf', 'TestFiles/Chapter 6.pdf']
#   output_pdf = 'merged.pdf'
#   merge_pdfs(pdf_paths, output_pdf)

