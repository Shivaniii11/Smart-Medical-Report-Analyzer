import streamlit as st
import pandas as pd
from pypdf import PdfReader
from PIL import Image
import ollama

from parser import extract_values
from charts import plot_data
from summary import generate_summary
from rag_engine import build_db
from ocr_engine import extract_text_from_image

st.set_page_config(page_title="Medical AI Offline", layout="wide")
st.title("🏥 Medical Report Intelligence System (Offline AI)")

# Upload
pdf_file = st.file_uploader("Upload PDF Report", type=["pdf"])
img_file = st.file_uploader("Upload Image Report", type=["png", "jpg", "jpeg"])

text = ""

# PDF
if pdf_file:
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

# IMAGE OCR
if img_file:
    image = Image.open(img_file)
    st.image(image, caption="Uploaded Report", use_container_width=True)
    text += extract_text_from_image(image)

# PROCESS
if text.strip():

    st.success("Report Processed Successfully ✅")

    df = extract_values(text)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Tests", len(df))

    with col2:
        abnormal = len(df[df["Status"] != "Normal"])
        st.metric("Abnormal", abnormal)

    with col3:
        score = max(0, 100 - abnormal * 10)
        st.metric("Health Score", score)

    st.subheader("📋 Extracted Values")
    st.dataframe(df, use_container_width=True)

    if not df.empty:
        st.plotly_chart(plot_data(df), use_container_width=True)

    st.subheader("🩺 Doctor Summary")
    st.write(generate_summary(df))

    db = build_db(text)

    st.subheader("🤖 Ask AI About Your Report")

    query = st.text_input("Ask medical question")

    if query:

        context = text

        if db:
            docs = db.similarity_search(query, k=3)
            context = "\n".join([doc.page_content for doc in docs])

        prompt = f"""
You are a friendly medical AI assistant.

Use report data below to answer correctly.

Rules:
- Give direct answer
- Explain simply
- Mention concerning values if relevant
- Suggest doctor if serious
- Do not repeat full report

Report:
{context}

Question:
{query}
"""

        response = ollama.chat(
            model="phi3",
            messages=[{"role": "user", "content": prompt}]
        )

        st.success(response["message"]["content"])

else:
    st.info("Upload report to begin.")