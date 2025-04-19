# Multi-Agent_Conversation_and_Stand-up_Comedy

This repository demonstrates how to build a simple multi-agent stand-up comedy interaction using Microsoft AutoGen and Groq’s low-latency LLM inference service. Two agents, **Tom** and **Nada**, exchange jokes in a conversational loop, with optional reflection-based summarization and termination logic.

---

## Features

- **Conversable Agents**: Uses `ConversableAgent` from AutoGen to define AI agents with customizable system messages, LLM configurations, and human-input modes.
- **Groq Integration**: Leverages the Groq API for fast inference, using models like `llama3-8b-8192` via environment-provided API key.
- **Multi-Turn Chat**: Demonstrates initiating conversations, retrieving chat history, cost metrics, and summaries.
- **Reflection Summaries**: Shows how to obtain refined conversation summaries via `reflection_with_llm`.
- **Termination Messages**: Illustrates custom termination logic for agents to end the chat gracefully.

---

## Prerequisites

- Python 3.7 or higher
- `pip` package manager
- A Groq API key (sign up at https://console.groq.com)

---

## Setup & Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
   ```

2. **Create & Activate a Virtual Environment**
   ```bash
   python -m venv venv
   # Windows PowerShell
   .\venv\Scripts\Activate.ps1
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   - Create a `.env` file in the project root with:
     ```env
     GROQ_API_KEY=your_actual_groq_api_key
     ```

---

## Usage

1. **Run the Comedy Script**
   ```bash
   python main.py
   ```

   This will:
   - Initialize **Tom** and **Nada** agents
   - Exchange two turns of jokes
   - Print the chat history, cost breakdown, and summary
   - Demonstrate an advanced reflection-based summary
   - Show termination logic in action

2. **Integrate into Your Own Code**
   - Import `ConversableAgent` and your `get_groq_api_key` utility.
   - Customize system messages, LLM config, and interaction patterns.

---





## Acknowledgments

- [Microsoft AutoGen](https://github.com/microsoft/autogen)
- [Groq Python Client](https://github.com/groq/groq-python)

