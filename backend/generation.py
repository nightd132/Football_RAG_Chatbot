def generate_answer(model, query, documents):
    context = "\n\n".join([doc.page_content for doc in documents])
    prompt = f"""Answer these questions based on the context below. If the answer is not contained within the context, say 'I don't know'. \n\n
            Context: {context}\n\n
            Question: {query}\n\n
    """
    response = model.invoke(prompt)
    return response