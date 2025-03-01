# My Django API Documentation  
This documentation provides details about the available endpoints in the API.

1. What is the API Key?
The API Key is a secret key that is required to access your API endpoints. It is used to authorize the frontend or any client making requests to your backend API.

2. Where to Include the API Key?
Usually, API keys are added to HTTP request headers.

In your Postman documentation, the API Key is mentioned under AUTHORIZATION.

👉 Your friend should add the API Key in the Headers section when making requests.

3. How to Include the API Key in Postman:
Tell your friend to follow these steps:

Go to Postman.
Select the request endpoint they want to test.
Click on the Headers tab.
Add the following key-value pair:
Key: Authorization
Value: API_KEY_VALUE (replace this with the actual API key you want to give them)
Example:

Key	Value
Authorization	your_api_key
4. How to Add in Code:
If your friend is using Axios or Fetch API in React, the header should be added like this:

Axios Example:
js
Copy
Edit
axios.get('https://your-ngrok-url/api/products/', {
  headers: {
    Authorization: 'your_api_key'
  }
})
.then(response => console.log(response.data))
.catch(error => console.error(error));
5. How to Test the API in Postman:
They can open your Postman Documentation URL.
Click on Run in Postman.
It will automatically import all endpoints into their Postman app.
They just need to add the API Key in the Headers before sending requests.
## Base URL
