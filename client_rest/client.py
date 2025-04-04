from fastapi import FastAPI
import uvicorn
import requests

app = FastAPI(title="Cliente REST Final")

GATEWAY_HOST = "gateway"
GATEWAY_PORT = 8000

@app.get("/")
def root():
    return {"message": "Cliente REST activo. Endpoints de prueba: /test_sum, /test_sub, /test_mul, /test_div"}

@app.get("/test_sum")
def test_sum(a: float, b: float):
    url = f"http://{GATEWAY_HOST}:{GATEWAY_PORT}/sum"
    params = {"a": a, "b": b}
    r = requests.get(url, params=params)
    return r.json()

@app.get("/test_sub")
def test_sub(a: float, b: float):
    url = f"http://{GATEWAY_HOST}:{GATEWAY_PORT}/sub"
    params = {"a": a, "b": b}
    r = requests.get(url, params=params)
    return r.json()

@app.get("/test_mul")
def test_mul(a: float, b: float):
    url = f"http://{GATEWAY_HOST}:{GATEWAY_PORT}/mul"
    params = {"a": a, "b": b}
    r = requests.get(url, params=params)
    return r.json()

@app.get("/test_div")
def test_div(a: float, b: float):
    url = f"http://{GATEWAY_HOST}:{GATEWAY_PORT}/div"
    params = {"a": a, "b": b}
    r = requests.get(url, params=params)
    return r.json()

if __name__ == "__main__":
    uvicorn.run("client:app", host="0.0.0.0", port=9000, reload=False)
