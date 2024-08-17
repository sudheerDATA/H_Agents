def get_weather(city: str):
    """
    Returns a hardcoded weather condition based on the provided city name.

    Parameters:
    city (str): The name of the city for which to retrieve the weather.

    Returns:
    str: A string representing the weather condition in the specified city.
    """
    
    # Check if the city is "California" and return "sunny" if it is.
    if city == "California":
        return "sunny"
    
    # Check if the city is "Paris" and return "rainy" if it is.
    if city == "Paris":
        return "rainy"
    
    # Check if the city is "London" and return "cloudy" if it is.
    if city == "London":
        return "cloudy"
    
    # Check if the city is "New York" and return "sunny" if it is.
    if city == "New York":
        return "sunny"
    
    # Check if the city is "Toronto" and return "rainy" if it is.
    if city == "Toronto":
        return "rainy"



# def get_weather(city : str):
#     if city == "California":
#         return "sunny"
#     if city == "Paris":
#         return "rainy"
#     if city == "London":
#         return "cloudy"
#     if city == "New York":
#         return "sunny"
#     if city == "Toronto":
#         return "rainy"