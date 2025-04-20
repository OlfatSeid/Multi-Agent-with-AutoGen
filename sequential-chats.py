from autogen import ConversableAgent,initiate_chats
from utils import get_groq_api_key
import pprint

GROQ_API_KEY = get_groq_api_key()
llm_config = {
    "model": "llama3-8b-8192", 
    "api_key": GROQ_API_KEY,
    "api_type": "groq"
}




# Creating the agents
fitness_personal_agent = ConversableAgent(
    name="Fitness Personal Info Agent",
    system_message='''You are an enthusiastic fitness coach assistant.
    Collect the user's name, age, and location to personalize their experience.
    Only ask for these three pieces of information. 
    Return 'TERMINATE' when you have all details.''',
    llm_config=llm_config,
    human_input_mode="NEVER",
)

fitness_goal_agent = ConversableAgent(
    name="Fitness Goal Agent",
    system_message='''You are a certified fitness specialist.
    Gather information about:
    - Fitness goals (weight loss, muscle gain, endurance)
    - Current activity level
    - Preferred workout types (cardio, strength training, yoga)
    - Any physical restrictions
    Return 'TERMINATE' when you have sufficient information.''',
    llm_config=llm_config,
    human_input_mode="NEVER",
)

fitness_coach_agent = ConversableAgent(
    name="Personal Fitness Coach",
    system_message='''You are an AI-powered fitness expert. 
    Create personalized workout plans based on:
    1. User's demographic information
    2. Fitness goals
    3. Activity preferences
    Include exercise routines, rest days, and motivational tips.
    Keep the tone energetic and supportive!
    Return 'TERMINATE' when done.''',
    llm_config=llm_config,
    is_termination_msg=lambda msg: "terminate" in msg.get("content").lower(),
)

user_proxy = ConversableAgent(
    name="User Proxy",
    llm_config=False,
    human_input_mode="ALWAYS",
    is_termination_msg=lambda msg: "terminate" in msg.get("content").lower(),
)

# Configuring chat flow
fitness_chats = [
    {
        "sender": fitness_personal_agent,
        "recipient": user_proxy,
        "message": "Welcome to FitAI! Let's start with your name, age, and location.",
        "summary_method": "reflection_with_llm",
        "summary_args": {
            "summary_prompt": "Format response as JSON: {'name': '', 'age': '', 'location': ''}"
        },
        "max_turns": 2,
        "clear_history": True
    },
    {
        "sender": fitness_goal_agent,
        "recipient": user_proxy,
        "message": "Now, let's discuss your fitness goals and preferences...",
        "summary_method": "reflection_with_llm",
        "summary_args": {
            "summary_prompt": "Extract data as JSON: {'goals': '', 'activity_level': '', 'preferences': [], 'restrictions': ''}"
        },
        "max_turns": 3,
        "clear_history": False
    },
    {
        "sender": user_proxy,
        "recipient": fitness_coach_agent,
        "message": "Please create my personalized fitness plan!",
        "max_turns": 2,
        "summary_method": "last_msg",
    }
]



fitness_results = initiate_chats(fitness_chats)


for idx, result in enumerate(fitness_results):
    print(f"Session {idx+1} Summary:")
    print(result.summary)
    print(f"Cost: {result.cost}\n")