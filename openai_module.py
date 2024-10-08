# Import the OpenAI class from the openai module. 
# This class is essential for interacting with OpenAI's API, enabling text generation and other AI tasks.
from openai import OpenAI

# Import the os module, which allows for interaction with the operating system, 
# including reading and setting environment variables.
import os

# Import the load_dotenv function from the dotenv module. 
# This function is used to load environment variables from a .env file into the application's environment.
from dotenv import load_dotenv

# Load environment variables from a .env file into the environment. 
# This function looks for a file named .env in the current directory and loads any variables defined there.
load_dotenv()

# Create an instance of the OpenAI class with the API key retrieved from environment variables.
# The API key is fetched using os.getenv, ensuring sensitive information is not hard-coded in the script.
# Create an object (instance) of the OpenAI class, which allows us to interact with OpenAI's API.
# The 'api_key' parameter is set by retrieving the API key from environment variables using os.getenv.
# This approach keeps the API key secure and avoids hard-coding sensitive information directly into the script.

# We are making a special tool (object) called 'openai_client' from a blueprint (class) called 'OpenAI'.
# This tool will help us talk to OpenAI's computer brain (API) and ask it to do things like answer questions.
# To use this tool, we need a secret key (like a password), which we get from a safe place (environment variables) using 'os.getenv'.
# By getting the secret key from this safe place, we make sure that our key is hidden and not written out in the open where anyone can see it.
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_text_basic(prompt: str, model="gpt-3.5-turbo", system_prompt: str="You are a helpful AI assistant"):
    """
    Generates a text response from the OpenAI model based on a single user prompt.
    
    Parameters:
    prompt (str): The user's prompt to which the AI should respond.
    model (str): The name of the model to use for generating the response. Default is "gpt-3.5-turbo".
    system_prompt (str): A system-level prompt that sets the behavior of the AI. Default is "You are a helpful AI assistant".
    
    Returns:
    str: The generated text response from the model.
    """
    # Call the OpenAI API to generate a completion based on the provided prompts and model.
    response = openai_client.chat.completions.create(
        model=model,  # Specify the model to use, default is "gpt-3.5-turbo".
        messages=[
            {"role": "system", "content": system_prompt},  # System prompt that sets the context for the AI's behavior.
            {"role": "user", "content": prompt}  # The user's input that the AI will respond to.
        ]
    )
    
    # Return the AI's generated response content.
    return response.choices[0].message.content

def generate_text_with_conversation(messages, model="gpt-3.5-turbo"):
    """
    Generates a text response from the OpenAI model based on a series of conversation messages.
    
    Parameters:
    messages (list): A list of dictionaries representing the conversation history, where each dictionary
                     has a "role" (e.g., "system", "user", "assistant") and "content" (the message text).
    model (str): The name of the model to use for generating the response. Default is "gpt-3.5-turbo".
    
    Returns:
    str: The generated text response from the model.
    """
    # Call the OpenAI API to generate a completion based on the provided conversation history and model.
    response = openai_client.chat.completions.create(
        model=model,  # Specify the model to use, default is "gpt-3.5-turbo".
        messages=messages  # The conversation history to pass to the AI for generating the next response.
    )
    
    # Return the AI's generated response content.
    return response.choices[0].message.content


"""
Project Description:
---------------------

This project demonstrates how to interact with OpenAI's API to generate text-based responses using different prompts. 
It includes two primary functions:

1. **generate_text_basic**: This function allows you to send a single prompt to the OpenAI model and get a response. 
   It also allows you to set a system-level prompt that guides the behavior of the AI. 
   For example, you can instruct the AI to act as a helpful assistant.

2. **generate_text_with_conversation**: This function is designed to handle more complex interactions 
   where there is a conversation history. The conversation is passed as a list of messages, 
   where each message has a role (e.g., "system", "user", "assistant") and content (the actual text). 
   The AI model uses this history to generate a more contextually relevant response.

**Environment Setup:**
----------------------

- The project uses the `dotenv` library to securely manage environment variables, 
  particularly for storing the OpenAI API key. This ensures that sensitive information 
  like API keys are not hard-coded into the script.

- Before running the script, make sure to create a `.env` file in the same directory as the script 
  and add your OpenAI API key in the following format:
  
**Usage:**
----------

- To generate a simple response based on a user prompt, use the `generate_text_basic` function.
- For more advanced conversational scenarios where you have multiple exchanges with the AI, 
use the `generate_text_with_conversation` function.

This project serves as a foundational example for anyone looking to integrate OpenAI's powerful 
language models into their applications, whether for simple text generation or more sophisticated 
conversational AI systems.
"""
