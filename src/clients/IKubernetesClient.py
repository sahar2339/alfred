from abc import ABC

class kubernetes_client(ABC):

    def get_Client(self) -> None:
        pass

    def get_pods(self, labels: dict = None, status_phase: str = None) -> list:
        pass

    def get_marked_nodes(self) -> list:
        pass

    def label_node(self, node: str, labels: dict) -> None:
        pass

    def cordon_node(self, node: str) -> None:
        pass

    def uncordon_node(self, node:str) -> None:
        pass

    def create_example_pod(self, node:str,  namespace: str) -> None:
        pass

    def delete_Pod(self, pod: str, namespace: str) -> None:
        pass

    def create_poison_pill(self, node:str, namespace: str) -> None:
        pass

    def get_poision_pill(self, namespace: str) -> list:
        pass
