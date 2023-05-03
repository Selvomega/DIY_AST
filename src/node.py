from node_type import NodeType

class Node:
    
    __head = ""
    __content = ""
    __child_array = []
    __separator_between_childs = "\n__separator_between_childs\n"

    def __init__(self,head=NodeType.NORMAL,content=""):
        self.__head = head
        self.__content = content
        if head != NodeType.NORMAL:
            self.__content = head.value

    def get_head(self):
        return self.__head
    
    def get_content(self):
        return self.__content
    
    def add_child(self,child_node):
        length = len(self.__child_array)
        self.__child_array[length] = child_node

    def generate_current_data(self):
        ret = ""
        for item in self.__child_array:
            ret = ret + item.get_content() + self.__separator_between_childs
        return ret
    