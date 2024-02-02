#pip install fastapi uvicorn

# 1. Library imports
import uvicorn
from fastapi import FastAPI

# 2. Create App object
app = FastAPI()

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Function for Top 10 Boxers
@app.get("/get_famous_boxer/{number}")
def get_famous_boxer(number: int):
    top_10_boxers = {
        1: "Muhammad Ali",
        2: "Mike Tyson",
        3: "Floyd Mayweather Jr.",
        4: "Manny Pacquiao",
        5: "Sugar Ray Robinson",
        6: "Rocky Marciano",
        7: "Joe Louis",
        8: "George Foreman",
        9: "Lennox Lewis",
        10: "Jack Dempsey"}
    if 1 <= number <= 10:
        return {number:top_10_boxers[number]}
    else:
        return {number:"We only know Top 10 boxers"}
    
    
# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
# uvicorn main:app --reload
