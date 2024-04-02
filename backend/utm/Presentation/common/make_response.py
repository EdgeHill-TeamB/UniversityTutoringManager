from fastapi.responses import JSONResponse
from fastapi import status
from pydantic import BaseModel
from typing import List, Dict


class ResponseMaker:
    @classmethod
    def from_dict(cls, data: Dict, model_class: BaseModel, status_code: int):
        serialized_data: BaseModel = model_class(**data).model_dump()
        return JSONResponse(content=serialized_data, status_code=status_code)

    @classmethod
    def from_list(cls, data: List, model_class: BaseModel, status_code: int):
        serialized_data = [model_class(**item).model_dump() for item in data]
        {
            "data": serialized_data,
            "number_of_records": len(serialized_data),
        }
        return JSONResponse(content=serialized_data, status_code=status_code)

    @classmethod
    def from_multitype(
        cls, data: Dict[str, List], model_classes: Dict[BaseModel], status_code: int
    ):
        serialized_data = {
            key: [model_classes[key](**item).model_dump() for item in value]
            for key, value in data.items()
        }
        return JSONResponse(content=serialized_data, status_code=status_code)
