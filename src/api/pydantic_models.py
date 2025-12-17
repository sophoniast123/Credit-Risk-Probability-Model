from pydantic import BaseModel
from typing import Dict, Union

class PredictionRequest(BaseModel):
    features: Dict[str, Union[str, float, int]]

class PredictionResponse(BaseModel):
    risk_probability: float
