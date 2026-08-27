from fastapi import FastAPI #import FastAPI class from fastapi module

# Create an instance of the FastAPI application.
# This 'app' object acts as the central server that handles incoming requests.
app = FastAPI()

#Tell FASTAPI to listen for incoming requests on GET root URL ("/")
@app.get("/")
def home ():
    return {"message": "Hello, FASTAPI!"}
