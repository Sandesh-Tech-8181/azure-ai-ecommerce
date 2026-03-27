# ADD THIS ENDPOINT (before the if __name__ line)
from pydantic import BaseModel

class SearchRequest(BaseModel):
    query: str
    limit: int = 5

@app.post("/api/v1/search")
async def search_products(request: SearchRequest):
    products = [{"id": "1", "name": f"AI Found: {request.query}", "price": 999}] * request.limit
    return {"products": products, "total": len(products)}