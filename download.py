import streamlit as st
from fpdf import FPDF
import base64
from io import BytesIO

def create_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    pdf_output = BytesIO()
    pdf.output(pdf_output, 'F')
    pdf_output.seek(0)
    return pdf_output

def get_binary_file_downloader_html(bin_file, file_label='File'):
    bin_str = base64.b64encode(bin_file).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{file_label}">Download {file_label}</a>'
    return href

st.title('Text to PDF Converter')

user_input = st.text_area("Enter the text you want to include in the PDF:", height=150)
if st.button('Create PDF'):
    if user_input:
        pdf_output = create_pdf(user_input)
        st.balloons()
        st.markdown(get_binary_file_downloader_html(pdf_output.getvalue(), "your_text.pdf"), unsafe_allow_html=True)
    else:
        st.error("Please enter some text to create the PDF.")