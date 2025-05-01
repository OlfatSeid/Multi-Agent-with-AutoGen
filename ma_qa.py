from autogen import ConversableAgent,GroupChat,GroupChatManager
from utils import get_groq_api_key


GROQ_API_KEY = get_groq_api_key()
llm_config = {
    "model": "deepseek-r1-distill-llama-70b", 
    "api_key": GROQ_API_KEY,
    "api_type": "groq"
}


router_agent = ConversableAgent(
    name="Router",
    system_message="""Determine if questions should use vectorstore or web search.
    - Vectorstore contains company knowledge base
    - Web search for external/current information
    Reply with ONLY 'vector' or 'web'""",
    llm_config=llm_config,
    max_consecutive_auto_reply=1
)

retriever_agent = ConversableAgent(
    name="Retriever",
    system_message="""Answer questions using ONLY vectorstore context.
    - Be concise and factual
    - Cite sources when available
    - If unsure, say 'I need to check'""",
    llm_config=llm_config,
    max_consecutive_auto_reply=2
)

web_searcher = ConversableAgent(
    name="WebSearcher",
    system_message="""Perform web searches for current information.
    - Use only trusted sources
    - Summarize key findings
    - Include source URLs""",
    llm_config=llm_config,
    max_consecutive_auto_reply=2
)

validation_agent = ConversableAgent(
    name="Validator",
    system_message="""Validate answers against these criteria:
    1. Relevance to original question
    2. Absence of hallucinations
    3. Source credibility
    4. Completeness of response
    Reply with 'APPROVED' or 'REJECTED' with reason""",
    llm_config=llm_config,
    max_consecutive_auto_reply=1
)


group_chat = GroupChat(
    agents=[router_agent, retriever_agent, web_searcher, validation_agent],
    messages=[],
    max_round=8,
    allowed_or_disallowed_speaker_transitions={
          router_agent: [retriever_agent, web_searcher],
        retriever_agent: [validation_agent],
        web_searcher: [validation_agent],
        validation_agent: [router_agent]
    },
    speaker_transitions_type="allowed"
)

manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config
)

def qa_workflow(question: str):
    """
    Execute full QA workflow:
    1. Routing decision
    2. Information retrieval
    3. Validation
    4. Final response
    """
    router_agent.initiate_chat(
        manager,
        message=question,
        clear_history=True
    )
    
  
    final_message = group_chat.messages[-1]["content"]
    return final_message if "APPROVED" in final_message else "Response needs refinement"

if __name__ == "__main__":
    question = "Should engineers bear moral responsibility for military AI?"

    result = qa_workflow(question)
    print(f"\nFinal Answer:\n{result}")