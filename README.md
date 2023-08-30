# IU FastAPI Services

## Introduction
This repository hosts the task given by IU (International University of Sciences). The task involves developing three FastAPI services to answer questions using a knowledge base while maintaining a conversation history.

## Components
The repository contains three services:

1. **Question-Answer Service**: Located in the `question_answer_service` directory. Takes a question and returns an answer.
  
2. **Answer Matching Service**: Located in the `answer_matching_service` directory. Takes a question and matches it to a relevant answer in a knowledge base.
  
3. **Conversation History Service**: Located in the `conversation_history_service` directory. Stores question and answer pairs into a knowledge base.

## Prerequisites
- Docker
- Docker Compose

## How to Run
1. Clone the repository:
```bash
git clone <repo_link>
```
2. Set the database URL:
```bash
export DB_URL=YOUR_DB_URL  # Example: sqlite:///commons/knowledge_base.db
```

3. Build and run the services:
```bash
docker-compose up
```


## API Endpoints
(TBD: describe endpoints here)

## Testing
(TBD)

## Troubleshooting
(TBD)

## Contributions
Feel free to submit pull requests or open issues to contribute to the project.

## License
(TBD)