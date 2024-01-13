import requests

# This function is called by your application after receiving the JSON object from OpenAI
def call_research_api(query):
    # Replace 'YOUR_API_ENDPOINT' with the actual endpoint of your research API
    api_endpoint = "http://localhost:10000"
    
    # Make the POST request to the research API with the query
    response = requests.post(api_endpoint, json={"query": query})
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response data
        data = response.json()
        # Format and return the data for presentation to the user
        return data
    else:
        # Handle any errors that occurred during the API call
        raise Exception(f"API call failed with status code {response.status_code}")

# Example usage of the function with a query parameter
query_param = input("Enter a query: ")
research_data = call_research_api(query_param)
print(research_data)
