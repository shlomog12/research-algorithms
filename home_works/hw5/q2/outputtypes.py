from abc import ABC
from typing import Any, List, Callable


class OutputType(ABC):

    @classmethod
    def extract_output_from_list_of_nodes(cls, nodes: List[Any]):
        """
        Construct and return a Bins structure. Used at the initialization phase of an algorithm.
        """
        raise NotImplementedError("Choose a specific output type")



class Count(OutputType):
    """ Output the list of sums of all bins (but not the bins' contents).  """

    @classmethod
    def extract_output_from_list_of_nodes(cls, nodes: List[Any]) -> Any:
        return len(nodes)


class SortedNodes(OutputType):
    """ Output the list of sums of all bins (but not the bins' contents).  """

    @classmethod
    def extract_output_from_list_of_nodes(cls, nodes: List[Any]) -> Any:
        return sorted(nodes)


class ListOfNodes(OutputType):
    """ Output the list of sums of all bins (but not the bins' contents).  """

    @classmethod
    def extract_output_from_list_of_nodes(cls, nodes: List[Any]) -> Any:
        return nodes


