from abc import ABC
from typing import Any, List, Callable

class OutputType(ABC):

    @classmethod
    def extract_output_from_list_of_nodes(cls, nodes: List[Any]):
        """
        return Output by type and by list of nodes
        """
        raise NotImplementedError("Choose a specific output type")

class Count(OutputType):
    """ 
    Returns the number of vertices in a connected component
    """

    @classmethod
    def extract_output_from_list_of_nodes(cls, nodes: List[Any]) -> int:
        return len(nodes)

class SortedNodes(OutputType):
    """ 
    Returns the sorted vertices
    """

    @classmethod
    def extract_output_from_list_of_nodes(cls, nodes: List[Any]) -> List[Any]:
        return sorted(nodes)


class ListOfNodes(OutputType):
    """ Returns the list of vertices in the order they were passed in the algorithm """

    @classmethod
    def extract_output_from_list_of_nodes(cls, nodes: List[Any]) -> List[Any]:
        return nodes


