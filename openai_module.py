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
