import os
import requests
import streamlit as st
import json
from dotenv import load_dotenv
from datetime import datetime
import pandas as pd
import numpy as np


# Load environment variables
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")


# Agent types
agent_types = {
    "Assistants": [
        "Personal Healthcare Assistant",
        "Retail Shopping Assistant",
        "Banking Assistant"
    ],
    "Research Agents": [
        "Medical Literature Analyzer",
        "Customer Sentiment Tracker",
        "Fraud Pattern Researcher"
    ],
    "Content Generators": [
        "Healthcare Report Generator",
        "Retail Product Descriptions",
        "Compliance Report Generator"
    ]
}


# Unified prompt template
prompt_template = (
    "Generate 3 high-impact and realistic Agentic AI use cases in the {domain} domain "
    "for the following user persona. Focus on solving the specific pain point within the "
    "provided constraints.\n\n"
    "Persona: {persona}\n"
    "Pain Point: {pain_point}\n"
    "Constraints: {constraints}\n\n"
    "Use a clear and concise format with numbered use cases."
)


# Fallback use cases in case of API failure or offline mode
fallback_use_cases = {
    "Healthcare": [
        "1. Agentic AI for automated patient intake, gathering symptoms, and scheduling appointments.",
        "2. AI assistant for doctors that summarizes patient history and suggests next steps.",
        "3. AI-powered compliance agent to ensure hospital procedures follow regulations."
    ],
    "Retail": [
        "1. AI-driven shelf restocking agent that tracks stock levels and automatically reorders items.",
        "2. Virtual shopping assistant that recommends outfits based on user preferences.",
        "3. Customer service AI that handles refunds and product queries autonomously."
    ],
    "Banking": [
        "1. Agentic fraud detection bot that scans transactions and flags anomalies in real-time.",
        "2. AI loan assistant that evaluates applicants and explains rejections based on policy.",
        "3. Agent that monitors customer spending habits and suggests financial optimizations."
    ]
}


def generate_use_cases(domain, persona, pain_point, constraints="None"):
    prompt = prompt_template.format(
        domain=domain,
        persona=persona,
        pain_point=pain_point,
        constraints=constraints or "None"
    )


    # Offline mode or missing token fallback
    if HF_TOKEN is None:
        st.warning("⚠️ No Hugging Face token found. Using fallback use cases.")
        return "\n".join(fallback_use_cases.get(domain, ["Use case generation failed."]))


    api_url = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {"inputs": prompt}


    try:
        response = requests.post(api_url, headers=headers, json=payload)
        if response.status_code == 200:
            generated = response.json()[0]["generated_text"]
            return generated.split("Use a clear and concise format with numbered use cases.")[-1].strip()
        else:
            st.warning("⚠️ API call failed. Using fallback use cases.")
            return "\n".join(fallback_use_cases.get(domain, ["Use case generation failed."]))
    except Exception as e:
        st.error("❌ Error: " + str(e))
        return "\n".join(fallback_use_cases.get(domain, ["Use case generation failed."]))


# Streamlit UI
st.title("🎯 Agentic AI Use Case Generator (Healthcare, Retail, Banking)")
st.markdown("Generate **high-impact Agentic AI use cases** based on persona, domain, and pain points.")


with st.expander("🧠 Explore Agent Types"):
    for category, agents in agent_types.items():
        st.markdown(f"**{category}:**")
        st.write(", ".join(agents))


with st.form("use_case_form"):
    domain = st.selectbox("Select Domain", ["Healthcare", "Retail", "Banking"])
    persona = st.text_input("User Persona (e.g., 'Hospital Administrator')")
    pain_point = st.text_input("Pain Point (e.g., 'manual data entry')")
    constraints = st.text_input("Constraints (Optional)", placeholder="e.g., cost limit, compliance, etc.")


    submitted = st.form_submit_button("🚀 Generate Use Cases")


if submitted:
    if not persona or not pain_point:
        st.warning("Please fill in both the Persona and Pain Point fields.")
    else:
        with st.spinner("Generating use cases..."):
            output = generate_use_cases(domain, persona, pain_point, constraints)


        st.subheader("✅ Generated Use Cases")
        st.text_area("Results", output, height=200)


        st.download_button("⬇️ Download as JSON", json.dumps({
                "domain": domain,
                "persona": persona,
                "pain_point": pain_point,
                "constraints": constraints,
            "output": output
        }, indent=2), file_name="agentic_use_cases.json", mime="application/json")


        st.download_button("⬇️ Download as Markdown", f"""# Agentic AI Use Cases


**Domain:** {domain}  
**Persona:** {persona}  
**Pain Point:** {pain_point}  
**Constraints:** {constraints or "None"}


## Use Cases
{output}
""", file_name="agentic_use_cases.md", mime="text/markdown")