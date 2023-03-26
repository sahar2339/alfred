from pydantic import BaseModel


class UnhealthyPod(BaseModel):
    pod_name: str
    namespace: str


class Pod(BaseModel):
    pod_name: str
    namespace: str
    node_name: str
