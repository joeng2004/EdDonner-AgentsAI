#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime

from stock_picker.crew import StockPicker

# To read in the .env environment variables
from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())
load_dotenv(override=True)


base_url = os.getenv("BASE_URL")

# Set the environment variables that CrewAI/litellm expects
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_BASE"] = base_url
os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY")

print(f"Base URL: {base_url}")  # Your existing debug line




warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the research crew.
    """
    inputs = {
        'sector': 'Technology',
        "current_date": str(datetime.now())
    }

    # Create and run the crew
    result = StockPicker().crew().kickoff(inputs=inputs)

    # Print the result
    print("\n\n=== FINAL DECISION ===\n\n")
    print(result.raw)


if __name__ == "__main__":
    run()
