# Reflection and Blogpost Writing:
#------------------------------
import streamlit as st
import autogen
from autogen import AssistantAgent
from utils import get_groq_api_key
import json


st.title("AI-Powered Blog Post Generator")
st.subheader("Generate and Refine Content with AutoGen Agents")


GROQ_API_KEY = get_groq_api_key()
llm_config = {
    "model": "llama3-8b-8192", 
    "api_key": GROQ_API_KEY,
    "api_type": "groq"
}

task = st.text_area("Enter your content request:",  height=150)
generate_button = st.button("Generate Blog Post")

def reflection_message(recipient, messages, sender, config):
    return f'''Review the following content: 
            \n\n {recipient.chat_messages_for_summary(sender)[-1]['content']}'''

if generate_button:
    with st.spinner("Generating and refining content..."):
        # Initialize agents
        writer = AssistantAgent(
            name="Writer",
            system_message="You are a professional writer. Create engaging content "
                        "and refine it based on feedback. Return only the final version.",
            llm_config=llm_config,
        )

        critic = AssistantAgent(
            name="Critic",
            system_message="You provide constructive feedback to improve content quality.",
            llm_config=llm_config,
        )

   
        reviewers = {
            "SEO Reviewer": "Optimize content for search engines (3 bullet points max)",
            "Legal Reviewer": "Ensure legal compliance (3 bullet points max)",
            "Ethics Reviewer": "Verify ethical soundness (3 bullet points max)"
        }

        # Create reviewer agents
        reviewer_agents = {}
        for name, prompt in reviewers.items():
            reviewer_agents[name] = AssistantAgent(
                name=name,
                system_message=f"You are a {name}. {prompt} Begin by stating your role.",
                llm_config=llm_config,
            )

        # Meta reviewer
        meta_reviewer = AssistantAgent(
            name="Meta Reviewer",
            system_message="Aggregate feedback from all reviewers and provide final suggestions.",
            llm_config=llm_config,
        )

        # Configure review chats
        review_chats = []
        for reviewer in reviewer_agents.values():
            review_chats.append({
                "recipient": reviewer,
                "message": reflection_message,
                "summary_method": "reflection_with_llm",
                "summary_args": {
                    "summary_prompt": "Return review as JSON: {'Reviewer': '', 'Review': ''}"
                },
                "max_turns": 1
            })

        review_chats.append({
            "recipient": meta_reviewer,
            "message": "Aggregate feedback and give final suggestions.",
            "max_turns": 1
        })

        # Register nested chats
        critic.register_nested_chats(review_chats, trigger=writer)

       
        result = critic.initiate_chat(
            recipient=writer,
            message=task,
            max_turns=2,
            summary_method="last_msg"
        )

       
        st.subheader("Final Blog Post")
        st.markdown(result.summary)

 
        st.subheader("Review Process")
        for msg in result.chat_history:
            if msg['name'] != 'Writer':
                try:
                    review_data = json.loads(msg['content'])
                    with st.expander(f"{review_data['Reviewer']} Feedback"):
                        st.write(review_data['Review'])
                except:
                    if "suggestion" in msg['content'].lower():
                        with st.expander("Meta Reviewer Final Suggestions"):
                            st.write(msg['content'])