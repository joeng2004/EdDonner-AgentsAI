#!/usr/bin/env python
import sys
import warnings
import os

from dotenv import load_dotenv, find_dotenv

# Loads environment variables from .env file at the project root
load_dotenv(find_dotenv())

api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("BASE_URL")

# Set the environment variables that CrewAI/litellm expects
os.environ["OPENAI_API_KEY"] = api_key
if base_url:
    os.environ["OPENAI_API_BASE"] = base_url


from datetime import datetime

from debate.crew import Debate

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'motion': 'There needs to be strict laws to regulate LLMs',
    }
    
    try:
        result = Debate().crew().kickoff(inputs=inputs)
        print(result.raw)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
