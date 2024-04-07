import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db.database import engine
from db.database import Base
from routes import(
    user, 
    auth,
    product,
) 

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.get("/", tags=["Home"])
def home():
    return "Server is running!!!"


app.include_router(user.router, prefix="/api")
app.include_router(auth.router, prefix="/api")
app.include_router(product.router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)


