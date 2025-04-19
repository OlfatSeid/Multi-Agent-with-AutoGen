## Multi-Agent_Conversation_and_Stand-up_Comedy

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









