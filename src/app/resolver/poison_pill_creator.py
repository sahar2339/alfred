from src.classes.resolver.resolver_interface import ResolverInterface
from src.models.node import UnhealthyNode


class PoisonPillCreator(ResolverInterface):
    def resolve(self, unhealthy_node: UnhealthyNode):
        pass
