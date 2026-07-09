# Football_RAG_Chatbot


## Overview

This project is about building a small RAG chatbot using local Ollama qwen2.5:3B model(because using Gemini free tier has limitation and other like OpenAi has free), which can answer some football question base on some external sources.

## Demo

![Demo](/images/Demo_Chat.gif)


## Prerequisite
- You will need download Ollama [here](https://ollama.com/download/windows)
- Then you need download model **qwen2.5:3B**:
```bash
    ollama run qwen2.5:3B
```
- And you need the embedding model:
```bash
    ollama pull nomic-embed-text
```

[!Note]
You can choose the model you want but have to change the model name in *config.py* in the *backend* folder. 

## Running Instruction
1. Open Terminal and run the backend:
```bash
cd backend
uvicorn api:app --reload
```

2. Open **new** Terminal and run the frontend
```bash
cd frontend
streamlit run app.py
```

And you now ready to go.