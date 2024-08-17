# Import the generate_text_basic function from a module named openai_module.
# This assumes that you have a Python file (module) named openai_module.py where
# the generate_text_basic function is defined and implemented.
from openai_module import generate_text_basic

# Define the prompt that will be sent to the AI model.
# In this case, the prompt is asking the AI to "Generate a 5 word sentence".
# prompt = "Generate a 6 word sentence"
prompt = "should i take umberalla in india in hyderabad"

# Call the generate_text_basic function with the defined prompt.
# This function interacts with the OpenAI API to generate a response based on the prompt.
response = generate_text_basic(prompt, model='gpt-4o')

# Print the generated response to the terminal.
# The response variable contains the AI-generated sentence, and this line will output it.
print(response)  # This should output the AI's response to the terminal
