# AI Research Assistant Agent 🤖

An AI-powered research assistant built with Python, Gemini, LangChain, and Streamlit. It answers general questions, performs mathematical calculations, and searches the web for current information.

## Features

- **AI-powered answers:** Uses Google's Gemini model to answer general questions.
- **Web search:** Retrieves web search results using DDGS.
- **Calculator:** Performs mathematical calculations using SimpleEval.
- **Conversation memory:** Maintains chat history during the current Streamlit session.
- **Interactive chat interface:** Built with Streamlit.
- **Clear Chat:** Allows users to reset the conversation.

## Tech Stack

- Python
- Google Gemini
- LangChain
- Streamlit
- DDGS
- SimpleEval
- python-dotenv

## Project Structure

```text
Agents_MYProject/
├── app.py
├── agent.py
├── tools.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup and Installation

1. Clone this repository:

   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   cd Agents_MYProject
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv myenv
   ```

   Windows PowerShell:

   ```powershell
   .\myenv\Scripts\Activate.ps1
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory and add your Gemini API key:

   ```text
   GOOGLE_API_KEY=your_api_key_here
   ```

   Replace `your_api_key_here` with your own API key. Never share or commit your actual API key.

5. Run the application:

   ```bash
   streamlit run app.py
   ```

## Example Questions

- What is machine learning?
- What is 125 * 24?
- What are the latest developments in Generative AI?

## Learning Outcomes

This project demonstrates practical experience with LLM integration, tool calling, agent creation, web search, conversation history, and building a user interface for an AI application.