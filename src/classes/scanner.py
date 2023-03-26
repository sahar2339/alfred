from src.clients.kube_client_interface import KubeClientInterface
from src.models.node import UnhealthyNode
from typing import List


class Scanner:
    def __init__(self, kube_client: KubeClientInterface):
        pass

    def get_unhealthy_nodes(self) -> List[UnhealthyNode]:
        pass
