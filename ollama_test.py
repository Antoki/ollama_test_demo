from ollama import chat, ChatResponse


if __name__ == "__main__":
    question = input("Ask something: ")
    stream = chat(
        model='llama3.2',
        messages=[{'role': 'user', 'content': question}],
        stream=True,
    )

    response: ChatResponse = chat(
        model='llama3.2',
        messages=[{'role': 'user', 'content': question}],
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

    print('\n\n')
    print(response.message)