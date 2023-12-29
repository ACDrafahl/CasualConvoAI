import speechToText

from gpt4all import GPT4All
model = GPT4All("mistral-7b-openorca.Q4_0.gguf")

# tokens = []
# output = model.generate("The opposite of up is ", max_tokens = 25)

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

with model.chat_session():
    i = 0
    while i < 3:
        prompt = input("Prompt") #speechToText.UserInput()
        output = model.generate(prompt=prompt, max_tokens=25, temp=0.7, top_k=40)
        print(output)
        i += 1
    # print(model.current_chat_session) # Prints the whole session



