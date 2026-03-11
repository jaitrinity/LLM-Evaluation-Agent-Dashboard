from openai import OpenAI

client = OpenAI()

def generate_answer(question, context):

    prompt = f"""
    Answer ONLY using the context.

    Context:
    {context}

    Question:
    {question}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content