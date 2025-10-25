from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.1:8b",
    validate_model_on_init=True,
    temperature=0.8,
    num_predict=256,
)
messages = [
    ("system", "You are helpfull sigma male explain user message"),
    ("human", "explain why llms are stupid"),
]

for chunk in llm.stream("Return the words Hello World!"):
    print(chunk.text(), end="")