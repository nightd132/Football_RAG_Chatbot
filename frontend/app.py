import streamlit as st

with st.sidebar:
    st.text('History')

answer = 'Here is the answer.'

prompt = st.chat_input("Ask me anything about Football, and I'll do my best to help you out!")
if prompt:
    st.chat_message("user").write(prompt)
    st.chat_message('assistant').write(answer)
