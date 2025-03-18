import streamlit as st
import requests

# Backend API URL
BACKEND_URL = "http://localhost:3001"

st.title("Web Content Q&A Tool")

# Input URLs
urls = st.text_area("Enter one or more URLs (one per line)").splitlines()

# Ingest URLs
if st.button("Ingest URLs"):
    if urls:
        response = requests.post(f"{BACKEND_URL}/ingest", json={"urls": urls})
        if response.status_code == 200:
            st.session_state["context"] = response.json()["content"]
            st.success("URLs ingested successfully!")
        else:
            st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
    else:
        st.warning("Please enter at least one URL.")

# Ask Questions
if "context" in st.session_state:
    question = st.text_input("Ask a question based on the ingested content")
    print(st.session_state["context"])
    if st.button("Ask"):
        response = requests.post(
            f"{BACKEND_URL}/ask",
            json={"question": question, "context": st.session_state["context"]},
        )
        if response.status_code == 200:
            st.success(f"Answer: {response.json()['answer']}")
        else:
            st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
