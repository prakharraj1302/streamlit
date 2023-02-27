import streamlit as st

st.set_page_config(page_title="Embedded PDF Demo")

# Define the URL of the PDF file you want to embed
pdf_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"

# Use the Streamlit IFrame component to embed the PDF
st.write(f'<iframe src="{pdf_url}" width="700" height="1000" frameborder="0"></iframe>', unsafe_allow_html=True)

