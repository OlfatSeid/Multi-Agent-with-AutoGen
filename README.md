## Multi-Agent_Conversation_and_Stand-up_Comedy

This repository demonstrates how to build a simple multi-agent stand-up comedy interaction using Microsoft AutoGen and Groq’s low-latency LLM inference service. Two agents, **Tom** and **Nada**, exchange jokes in a conversational loop, with optional reflection-based summarization and termination logic.

-----

## Features 🚀

- **Conversable Agents**: Uses `ConversableAgent` from AutoGen to define AI agents with customizable system messages, LLM configurations, and human-input modes.
- **Groq Integration**: Leverages the Groq API for fast inference, using models like `llama3-8b-8192` via environment-provided API key.
- **Multi-Turn Chat**: Demonstrates initiating conversations, retrieving chat history, cost metrics, and summaries.
- **Reflection Summaries**: Shows how to obtain refined conversation summaries via `reflection_with_llm`.
- **Termination Messages**: Illustrates custom termination logic for agents to end the chat gracefully.

---
## AI Fitness Coaching Assistant 🤖💪
Multi-agent conversational workflows for personalized fitness planning.

## Features 🚀

- **Multi-Stage Onboarding Process**
  - Personal Information Collection
  - Fitness Goal Assessment
  - Physical Restrictions Analysis
- **Smart Agent Orchestration**
  - Context-aware conversation flow
  - Automated history management
- **Personalized Recommendations**
  - Custom workout plans
  - Progress tracking suggestions
  - Motivational engagement tactics

## Prerequisites

- Python 3.7 or higher
- `pip` package manager
- A Groq API key ( https://console.groq.com)

---


# AI Blog Post Generator with AutoGen

An AI-powered blog post generation tool that uses multiple specialized agents to create and refine content through collaborative review.

## Overview

This application combines Streamlit's interactive interface with AutoGen's multi-agent system to:
- Generate initial blog post drafts
- Conduct specialized reviews (SEO, Legal, Ethics)
- Provide aggregated feedback
- Produce polished final content

## Features 🚀

🛠️ **AI Agent Collaboration**
- Writer agent for content creation
- Critic agent for quality feedback
- Specialized reviewers (SEO, Legal, Ethics)
- Meta-reviewer for final suggestions

🔍 **Multi-stage Review Process**
- Automated content optimization
- Compliance checks
- Ethical validation
- Search engine optimization

📊 **Interactive Interface**
- Real-time generation tracking
- Expandable review sections
- Clean output formatting
- User-defined content prompts
------------------------------------------
# Conversational Chess with AI Agents

A chess implementation where AI agents play against each other using natural language and tool calls, powered by AutoGen.

## Features 🚀

- 🤖 Two AI players (White & Black) with separate identities
- ♟️ Real chess board visualization using `python-chess`
- 🛠️ Tool-based interaction for legal moves and move execution
- 💬 Natural language chitchat between moves
- 🔄 Automatic turn management with nested conversations
- 🖥️ SVG board visualization with move highlights


--------------------------------

# Automated Stock Analysis 

## Overview
This project demonstrates an AI-powered stock analysis system using Microsoft's AutoGen framework and Groq's accelerated AI computing. The system autonomously generates stock performance visualizations through collaborative AI agents.

## Features
- **AI Agent Collaboration**: Uses Writer and Executor agents for code generation/execution
- **YTD Performance Analysis**: Automated year-to-date stock comparisons
- **Volatility Visualization**: Scatter plots with risk-return relationships
- **Multi-Ticker Support**: Compare multiple stocks simultaneously
- **Auto-Saving Results**: Plots saved as high-resolution PNG files
- **Safety Protocols**: Code execution timeouts and human verification

**Usage**

The system will:

Initialize AI agents

Fetch stock data from Yahoo Finance

Generate analysis plots

Save visualizations to /coding directory

Example outputs:

ytd_stock_gains.png: Normalized YTD comparison

stock_prices_YTD_plot.png: Price timeline

volatility_analysis.png: Risk-return scatter plot

---------------------------------------------------

# Planning and Stock Report Generation
This notebook demonstrates a multi-agent system  to collaboratively research, analyze, and write a blog post about stock price performance.

## Features

- 🤖 Multi-agent collaboration with distinct roles
- 📈 Automated stock data retrieval and analysis
- 📝 AI-powered blog post generation
- 🔄 Iterative refinement process

#### Build a group chat

This group chat will include these agents:

1. **User_proxy** or **Admin**: to allow the user to comment on the report and ask the writer to refine it.
2. **Planner**: to determine relevant information needed to complete the task.
3. **Engineer**: to write code using the defined plan by the planner.
4. **Executor**: to execute the code written by the engineer.
5. **Writer**: to write the report.

#### Customization Options

- Change target company (update task variable)
- Modify date range (adjust "past year" in task)
- Add technical indicators to analysis
- Customize blog post format/tone

--------------------------------------------------------
#  Multi-Agent Question Answering with DeepSeek

A question-answering system that routes queries between knowledge bases and web searches, with validation mechanisms.

## Features
- Dynamic question routing (vectorstore vs web search)
- Hallucination detection
- Source credibility validation
- Ethical safeguard recommendations
----------------

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
**License**  
Distributed under the MIT License. See [LICENSE](LICENSE) for full terms.
