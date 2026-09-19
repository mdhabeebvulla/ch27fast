from fastapi import FastAPI
import joblib
app = FastAPI()
@app.get("/")
def predict_iris(sl:float,sw:float,pl:float,pw:float):
  model = joblib.load("mymodel")
  result = model.predict([[sl,sw,pl,pw]])
  return {"predcition is ":int(result[0])}
  
