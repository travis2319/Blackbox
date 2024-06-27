import requests

# The base URL of your Google Apps Script web app
base_url = "https://script.google.com/macros/s/AKfycbwVR6GLTTL99a4dFJazRhK-0fBl9YMY6kkyGrdJoYbXsVs_bp8xJo_tQgKcxvoMO46CLw/exec"

# The data you want to add
value1 = "123"
value2 = "456"
value3 = "789"

# Construct the full URL with query parameters
full_url = f"{base_url}?value1={value1}&value2={value2}&value3={value3}"

# Send the GET request
response = requests.get(full_url)

# Check if the request was successful
if response.status_code == 200:
    print("Data successfully sent to Google Sheets")
else:
    print(f"Failed to send data. Status code: {response.status_code}")
    print(f"Response content: {response.text}")