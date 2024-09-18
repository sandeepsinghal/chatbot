from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage


# Initialize the model
model = ChatOpenAI(model="gpt-3.5-turbo")

# Function to handle conversation with history
def chat_with_history(history, new_message):
    # Add the new message to the history
    history.append(HumanMessage(content=new_message))

    # Invoke the model with the updated history
    ai_message:AIMessage = model.invoke(history)

    # Add the model's response to the history
    history.append(AIMessage(content=ai_message.content))

    return ai_message.content, history

# Initialize conversation history
conversation_history = []

# Interactive loop
print("Start chatting with the AI (type 'exit' to stop):")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response, conversation_history = chat_with_history(conversation_history, user_input)
    print("AI:", response)