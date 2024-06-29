### Project Goals:
- To demo a simple FARM stack project, using MongoDB Atlas Cloud, FastAPI, and React.
- Create a To-Do app with full CRUD that can easily manage a user's tasks, persist them to a database, and render them in the browser

### To run this project:
- ensure MongoDB Atlas cluster is actie and configured properly
- activate virtual environment: `source .venv/bin/activate'
- cd to backend, run: `uvicorn main:app --reload`
- cd to frontend, open a new terminal and run: `npm run dev`
- Swagger UI can be accessed at localhost:8000/docs

### Next steps:
- Dockerize it into 3 containers:
* MongoDb
* API
* Client

- unit tests
- integration testing
- CI/CD
- Add more features/ broaden functionality
