def generate_answer(model, query, documents):
    print(len(documents))
    if len(documents) > 0:
        context = "\n".join([doc.page_content for doc in documents])
        prompt = f"""Answer these questions based on the context below. If the question is not relevant to Football ignore the context. If the question is about football and the answer is not contained within the context, say 'I don't know'.\n
                Context: {context}\n
                Question: {query}\n"""
    else:
        prompt = query
    response = model.invoke(prompt)
    return response.content