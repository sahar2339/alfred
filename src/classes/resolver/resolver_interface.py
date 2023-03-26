from abc import ABC, abstractmethod
from src.clients.kube_client_interface import KubeClientInterface
from src.models.node import UnhealthyNode


class ResolverInterface(ABC):
    def __init__(self, kube_client: KubeClientInterface):
        pass

    @abstractmethod
    def resolve(self, unhealthy_node: UnhealthyNode):
        pass

    def _pre_resolve(self, unhealthy_node: UnhealthyNode):
        pass
