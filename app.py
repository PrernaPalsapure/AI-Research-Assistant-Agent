import streamlit as st

from agent import agent


st.title("🤖 AI Research Assistant")


if "messages" not in st.session_state:
    st.session_state.messages = []


if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# Chat input
question = st.chat_input("Ask me anything...")


if question:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    # Display user message
    with st.chat_message("user"):
        st.write(question)


    # Send conversation to agent
    result = agent.invoke({
        "messages": st.session_state.messages
    })


    answer = result["messages"][-1]

    answer_text = answer.content[0]["text"]


    # Save assistant message
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer_text
    })


    # Display assistant message
    with st.chat_message("assistant"):
        st.write(answer_text)