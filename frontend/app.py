import streamlit as st
import requests

prompt = st.chat_input("Ask me about Football, and I'll do my best to help you out!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    request = requests.post("http://localhost:8000/chat", json={"query": prompt})
    response = request.json()
    answer = response["answer"]
    sources = "\n".join(response["sources"]) 
    answer_message = (answer + "\n\nSources: \n\n" +sources) if len(response["sources"]) > 0 else answer
    with st.chat_message('assistant'):
        st.markdown(answer_message)
    st.session_state.messages.append({"role": "assistant", "content": answer_message})
