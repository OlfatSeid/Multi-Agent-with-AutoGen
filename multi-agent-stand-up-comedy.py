# Multi-Agent Conversation and Stand-up Comedy
#---------------------------------------------

from autogen import ConversableAgent
from utils import get_groq_api_key
import pprint

GROQ_API_KEY = get_groq_api_key()
llm_config = {
    "model": "llama3-8b-8192", 
    "api_key": GROQ_API_KEY,
    "api_type": "groq"
}

# Define an AutoGen agents:

nada= ConversableAgent(
    name="nada",
    system_message=
    "Your name is Nada and you are a stand-up comedian.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

tom= ConversableAgent(
    name="tom",
    system_message=
    "Your name is Tom and you are a stand-up comedian. "
    "Start the next joke from the punchline of the previous joke.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

chat_result = tom.initiate_chat(
    recipient=nada, 
    message="I'm Tom. Nada, let's keep the jokes rolling.",
    max_turns=2,
)
#------------------------------------------
## Print some results:
pprint.pprint(chat_result.chat_history)
print("*" * 50)

pprint.pprint(chat_result.cost)
print("*" * 50)

pprint.pprint(chat_result.summary)
print("*" * 50)



## Get a better summary of the conversation:
chat_result = tom.initiate_chat(
   nada, 
    message="I'm Tom. Nada, let's keep the jokes rolling.", 
    max_turns=2, 
    summary_method="reflection_with_llm",
    summary_prompt="Summarize the conversation",
)

pprint.pprint(chat_result.summary)

pprint.pprint(chat_result.summary)
#---------------------------------
# Chat Termination:
nada = ConversableAgent(
    name="Nada",
    system_message=
    "Your name is Nada and you are a stand-up comedian. "
    "When you're ready to end the conversation, say 'I gotta go'.",
    llm_config=llm_config,
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "I gotta go" in msg["content"],
)

Tom = ConversableAgent(
    name="Tom",
    system_message=
    "Your name is Tom and you are a stand-up comedian. "
    "When you're ready to end the conversation, say 'I gotta go'.",
    llm_config=llm_config,
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "I gotta go" in msg["content"] or "Goodbye" in msg["content"],
)


chat_result = tom.initiate_chat(
    recipient=nada,
    message="I'm Tom. Nada, let's keep the jokes rolling."
)

nada.send(message="What's last joke we talked about?", recipient=Tom)

