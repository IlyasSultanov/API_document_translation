from fastapi import FastAPI
from src.api.v1.endpoint import router
app = FastAPI()
app.include_router(router=router)



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)