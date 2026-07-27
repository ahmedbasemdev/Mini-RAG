from typing import Optional
from pydantic import BaseModel, Field, validator
from bson.objectid import ObjectId

class DataChunk(BaseModel):
    _id: Optional[ObjectId]  # this means that the _id field is optional and can be None
    chunk_text : str = Field(..., min_length=1) 
    chunk_metadata: dict
    chunk_order: int = Field(..., ge=0)  
    chunk_project_id: str = Field(..., min_length=1) 
