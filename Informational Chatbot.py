import streamlit as st
import openai
import asyncio

from openai import AsyncOpenAI

client = AsyncOpenAI(api_key=st.secrets["API_key"])

async def get_information(query):
    prompt_text = f"You asked: {query}"

    response = await client.chat.completions.create(
        model="text-davinci-003",  # Adjust model for informative response
        messages=[
            {"role": "system", "content": "I am Bard, your information assistant."},
            {"role": "user", "content": prompt_text}
        ],
    )

    return response.choices[0].message.content

def app():
    st.title("Informational Chatbot")

    if 'query' not in st.session_state:
        st.session_state.query = ""

    user_query = st.text_input("Ask me anything!")
    st.session_state.query = user_query

    if st.button("Get Information"):
        if st.session_state.query != "":
            st.experimental_rerun()  # Rerun app to show response

    if st.session_state.query != "":
        st.write("You asked:")
        st.write(st.session_state.query)
        st.write("Answer:")
        async def fetch_answer():
            answer = await get_information(st.session_state.query)
            st.write(answer)
        asyncio.run(fetch_answer())

if __name__ == "__main__":
    app()
