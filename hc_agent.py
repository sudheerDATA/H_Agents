# Import the generate_text_basic function from a custom module named openai_module.
# This function will be used to interact with the OpenAI API for generating text responses.
from openai_module import generate_text_basic

# Import a custom function get_weather from a module named sample_functions.
# This function is assumed to fetch the current weather conditions for a specified location.
from sample_functions import get_weather

# Call the get_weather function to retrieve the current weather conditions for California.
# The result is stored in the variable current_weather.
current_weather = get_weather("California")

# Define a prompt that will be sent to the AI model. 
# The prompt includes a question about whether to take an umbrella based on the weather conditions in California.
# The current weather conditions are dynamically inserted into the prompt using an f-string.
prompt = f"""
Should I take an umbrella when going out today in
California based on the following weather conditions: {current_weather}?"""

# Call the generate_text_basic function with the defined prompt.
# The model parameter is set to "gpt-4" to specify that the GPT-4 model should be used for generating the response.
response = generate_text_basic(prompt, model="gpt-4")

# Print the generated response to the terminal.
# This response will be the AI's advice on whether to take an umbrella based on the provided weather conditions.
print(response)

#------------------#---------------------#---------------
# #Hardcoded Agent
# from openai_module import generate_text_basic
# from sample_functions import get_weather

# current_weather = get_weather("California")

# prompt = f"""
# Should I take an umbrella when going out today in
# California based on the following weather conditions: {current_weather}?"""

# response = generate_text_basic(prompt,model="gpt-4")

# print(response)