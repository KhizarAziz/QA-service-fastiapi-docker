# We're getting FastAPI, a web framework to make APIs
from fastapi import FastAPI, Depends
# Importing Session to interact with the database
from sqlalchemy.orm import Session
# For text processing and finding similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np  # For number stuff like finding the maximum

# Importing our database and models
from commons.database import SessionLocal, engine
from commons import models

# Make the tables in the database
models.Base.metadata.create_all(bind=engine)

# Create the FastAPI app
app = FastAPI()

# This function gets a new database session
def get_db():
    db = SessionLocal()
    try:
        yield db  # Use the database
    finally:
        db.close()  # Close it when done

# This is our API endpoint. It matches questions!
@app.post("/match/")
def match_question(question: str, db: Session = Depends(get_db)):
    # Get questions and answers from the database
    questions_answers = db.query(models.QuestionAnswer).all()
    # Just the questions
    questions = [x.question for x in questions_answers]
    # Just the answers
    answers = [x.answer for x in questions_answers]
    
    # Add the new question to the list of old questions
    questions.append(question)

    # Turn text into numbers so the computer can understand
    vectorizer = CountVectorizer().fit_transform(questions)
    vectors = vectorizer.toarray()

    # Find out how similar the new question is to the old ones
    cosine_matrix = cosine_similarity(vectors)
    # Just the similarities for the new question
    similarity_scores = cosine_matrix[-1][:-1]

    # Find the old question that is most similar to the new one
    matched_index = np.argmax(similarity_scores)

    # Return the answer for the most similar old question
    return {"question": question, "answer": answers[matched_index]}
