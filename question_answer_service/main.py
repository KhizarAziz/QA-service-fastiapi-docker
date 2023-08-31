# Import FastAPI and HTTP library
from fastapi import FastAPI, HTTPException
import requests  # To make HTTP requests to our second API
from commons import constants
# Initialize our FastAPI app
app = FastAPI()

# This is our single API endpoint to accept user's questions
@app.get("/ask/")
def ask_question(question: str):
    # URL for our second API service
    matching_service_url = constants.QA_MATCHING_SERVICE
    
    # Trying to get answer from the second API
    try:
        # Make the POST request to the second API and get response
        response = requests.post(matching_service_url, json={"question": question})
        
        # Convert JSON response to Python dictionary
        result = response.json()
        
        if result.get('answer_found'):
            answer = result.get('answer') # Fetch the answer from the response dictionary
        else:
            answer = "No Answer Found!"

        # Return the final answer
        return {"question": question, "answer": answer}
        
    except Exception as e:
        # If something went wrong, let's tell the user
        raise HTTPException(status_code=500, detail=str(e))
