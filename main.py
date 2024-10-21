from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
templete = """
Answer the question below.
Here is the conversation history: {context}
Question: {question}
Answer:
"""
model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(templete)
chain = prompt | model
def handle_conversation():
    context = ""
    print("Welcome to AI chatbot type 'exit' to exit")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({'context':context,'question':user_input})
        print("Bot: ",result)
        context += f"\n User: {user_input}\nAI: {result}"
if __name__ == "__main__":
    handle_conversation()

""" When explaining your choice of libraries and modules for creating a simple text-based chatbot, you may highlight
the following points:

1. Langchain: Langchain is an open-source Python library designed to make it easy to build various types of AI
applications, including chatbots. It provides pre-built prompts and chains for common tasks like asking questions
and generating responses, making it an ideal choice for creating a simple text-based chatbot quickly.
2. Langchain-Ollama: The `langchain_ollama` library is an extension of the core Langchain library, specifically
tailored to work with the Ollama model. As you're using the Ollama model for your chatbot, it makes sense to use
this library to leverage its specific features and simplify the process of integrating the model into your
application.
3. `OllamaLLM`: The `OllamaLLM` class from the `langchain_ollama` library is a wrapper around the Ollama model,
making it easy to use the model in your chatbot. It provides methods for loading models and generating responses
given a prompt.
4. `ChatPromptTemplate`: This module helps create prompts that can be used with various language models like the
one provided by Langchain-Ollama. You're using it to structure the conversation between the user and the chatbot.
5. The template defined in your code includes a context and question, making it easy for the model to understand
the conversation history and focus on providing relevant responses based on the current question. This helps
create a more natural-sounding conversation.
6. By using this library and its specific components, you're able to quickly build a simple text-based chatbot
that can answer questions and carry on a conversation with minimal effort and code."""