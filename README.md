# FastAPI Tutorial

Creating APIs using FastAPI lives up to it's name. You can easily create APIs of your python functions within a few minutes

## Steps to follow
* Install the Libraries
  ```python
    pip install fastapi uvicorn -q
* Import the Libraries in your Python file (main.py) <br>
  ```python
  import uvicorn
  from fastapi import FastAPI
* Create App object
  ```python
  app = FastAPI()
* Create a function that runs when the App is opened
  ```python
  @app.get('/')
  def index():
      return {'message': 'Dont Look At Me!'}
* Run the API with uvicorn
  ```python
    if __name__ == '__main__':
      uvicorn.run(app, host='127.0.0.1', port=8000)
* In the terminal/shell/bash/whatever use the following command to run your main.py App
  ```python
    uvicorn main:app --reload
* Open the following URL in your browser and you'd see the "Index function" displaying whatever you returned
  ```python
    http://127.0.0.1:8000
* While your App is running you can use your API in any Python/Jupyter file anywhere on your local system by simply using the following:
  ```python
    import requests
    api_url = "http://127.0.0.1:8000/index"
    response = requests.get(api_url)
    print(response)
