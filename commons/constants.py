import os

DB_URL = os.environ.get('DB_URL')

QA_MATCHING_SERVICE = "http://localhost:8001/match/"
TABLE_QA = "questions_answers"