from pydantic import BaseModel
from typing import List
from src.models.pod import UnhealthyPod


class UnhealthyNode(BaseModel):
    node_name: str
    unhealthy_pods: List[UnhealthyPod]
