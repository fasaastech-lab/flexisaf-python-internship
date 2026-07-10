import requests

# URL of the public API to call
url = "https://httpbin.org/get"

try:
    # Make a GET request with a 5 second timeout
    response = requests.get(url, timeout=5)
    
    # Raise an error if server returned 4xx or 5xx status
    response.raise_for_status()
    
    # Convert response to Python dictionary
    data = response.json()
    print("Request successful")
    print(data)

except requests.exceptions.ConnectionError:
    # Handle no internet connection
    print("Network error: Could not connect to the server")

except requests.exceptions.Timeout:
    # Handle server taking too long to respond
    print("Error: The request timed out")

except requests.exceptions.HTTPError as e:
    # Handle server errors like 404 or 500
    print(f"HTTP error: {e}")

except Exception as e:
    # Handle any other unexpected error
    print(f"Unexpected error: {e}")