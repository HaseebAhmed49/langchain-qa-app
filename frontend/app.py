import streamlit as st
import requests


st.title("🧠 LangChain Q&A App")

question = st.text_input("Ask a question:")
if st.button("Get Answer"):
  response = requests.post("http://127.0.0.1:8000/ask", json={"question": question})
  st.write("Answer:", response.json().get("answer"))
