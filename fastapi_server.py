# main.py
from fastapi import FastAPI
import asyncio # For simulating async I/O

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/")
async def read_root():
    await asyncio.sleep(0.01) # Simulate a small async I/O delay
    return {"message": "Hello, FastAPI from /"}

@app.get("/slow_sync")
def slow_sync_endpoint():
    import time
    time.sleep(0.1) # Simulate a blocking CPU or synchronous I/O
    return {"message": "This was a synchronous, potentially blocking call handled in a thread pool."}

@app.get("/async_io_long")
async def async_io_long():
    # Simulate a longer async I/O operation
    await asyncio.sleep(1)
    return {"message": "This was a longer async I/O operation."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5002)