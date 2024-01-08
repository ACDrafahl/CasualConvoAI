from gpt4all import GPT4All
model = GPT4All("C:\Users\acdga\.cache\gpt4all\mistral-7b-openorca.Q4_0.gguf")
# tokens = []
# output = model.generate("The opposite of up is ", max_tokens = 25)
with model.chat_session():
    i = 0
    while i < 3:
        prompt = input("Prompt: ")
        output = model.generate(prompt=prompt, max_tokens=25, temp=0.7)
        print(output)
        i += 1
    # print(model.current_chat_session) # Prints the whole session

    ''' With tokens
    i = 0
    while i < 3:
        prompt = input("Prompt: ")
        for token in model.generate(prompt=prompt, max_tokens=25, temp=0.7, streaming=True):
            tokens.append(token)
        print(tokens)
        i += 1
    # print(model.current_chat_session) # Prints the whole session
    '''

