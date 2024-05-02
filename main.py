import streamlit as st
from fpdf import FPDF

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
        st.download_button("Download PDF", "output.pdf")

if __name__ == "__main__":
    main()