from .kubernetesClient import kubernetes_client
from openshift.dynamic import DynamicClient
from kubernetes.client import ApiClient, configuration
from src.models import ObjectKinds
from ..utils.k8s_utils  import time_passed_since_created

SECONDS_PASSED_POD_STUCK = 180 

KINDS_API_VERSIONS = {
    ObjectKinds.POD: "v1",
    ObjectKinds.NODE: "v1"
}

class openshift_client(kubernetes_client):
    def __init__(self, host:str, token: str, verify_ssl: bool = False) -> None:
        super().__init__()
        self.host = host
        self._token = token
        self._config = self._init_config(verify_ssl)
        self.dynamic_client = self._init_dynamic_cleint()
        
    def __init_config(self, verify_ssl: bool = False) -> configuration:
        config = configuration(self.host)
        config.api_key['authorization'] = self._token
        config.api_key_prefix['authorization'] = 'Bearer'
        config.verify_ssl - verify_ssl
        return config
    
    def __init_dynamic_client(self) -> DynamicClient:
        api_client = ApiClient(self._config)
        return DynamicClient(api_client)
    
    def __make_payload(self, **data) -> DynamicClient:
        return {key: value for key, value in data.items() if value}
    
    def __get_object_or_objects(self, kind: ObjectKinds, namespace: str, name: str  = None, labels: str = None) -> None:
        resource_client = self.dynamic_client.resources.get(
            api_version=KINDS_API_VERSIONS[kind],
            kind=kind
        )
        payload = self.__make_payload(
            namespace=namespace,
            label_selector=labels,
            name=name
        )
        return resource_client.get(**payload)


    def __delete_object(self, kind: ObjectKinds, namespace:str, name:str) -> None:
        resource_client = self.dynamic_client.resources.get(
            api_version = KINDS_API_VERSIONS[kind],
            kind = kind
        )
        return resource_client.delete(
            namespace = namespace,
            name = name
        )

    def __create_object(self, kind: ObjectKinds, body: dict, namespace: str = None):
        resource_client = self.dynamic_client.resources.get(
            api_version = KINDS_API_VERSIONS[kind],
            kind = kind
        )
        payload = self.__make_payload(
            body=body,
            namespace=namespace
        )
        return resource_client.create(**payload)
    
    def __update_object(self, kind: ObjectKinds, name: str, body:dict, namespace:str=None):
        resource_client = self.dynamic_client.resources.get(
            api_version = KINDS_API_VERSIONS[kind],
            kind = kind
        )
        payload = self.__make_payload(
            body=body,
            name=name,
            namespace=namespace
        )
        return resource_client.patch(**payload)

    def get_poision_pill(self, namespace: str) -> list:
        self.get_object_or_objects()

    def get_pods(self, namespace: str, labels: dict = None, status_phase: str = None) -> list:
        stuck_pods = []
        pods = self.__get_object_or_objects(ObjectKinds.POD, namespace, labels=labels)
        for pod in pods:
            if "containerStatuses" not in pod["status"].keys():
                continue
            
            if time_passed_since_created(pod.to_dict()) <= SECONDS_PASSED_POD_STUCK:
                stuck_pods.append({"name":"pod"})

            


 