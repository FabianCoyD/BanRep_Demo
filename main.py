import streamlit as st
from fpdf import FPDF
import os

def create_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=text)
    pdf.output("output.pdf")

def main():
    st.title("Text to PDF Converter")
    st.write("Enter your text below:")
    text = st.text_area("Text", height=200)
    if st.button("Create PDF"):
        create_pdf(text)
        st.success("PDF created successfully!")
        with open("output.pdf", "rb") as file:
            btn = st.download_button(
                "Download PDF",
                file,
                file_name="output.pdf",
                mime="application/pdf",
            )

if __name__ == "__main__":
    main()