from fastapi import FastAPI

app = FastAPI(title="Gestão de Escalas")


@app.get("/health")
def health():
    return {"status": "ok"}