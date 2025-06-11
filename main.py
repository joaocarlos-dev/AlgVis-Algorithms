from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sorts.routes import router as sorts_router

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Backend de algoritmos rodando!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(sorts_router, prefix="/sorts")
