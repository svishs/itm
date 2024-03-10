from fastapi import FastAPI
from operations.router import router as router_operation
from pages.router import router as router_pages
import uvicorn

app = FastAPI(title="OCR service")

app.include_router(router_operation)
app.include_router(router_pages)


if __name__ =='__main__':
    uvicorn.run('main:app')