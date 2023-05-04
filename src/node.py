from node_type import NodeType

class Node:

    def __init__(self,head=NodeType.NORMAL,content=""):
        self.__head = head
        self.__content = content
        self.__child_array = []
        self.__separator_between_childs = "\n__separator_between_childs\n"

    def get_head(self):
        return self.__head
    
    def get_content(self):
        return self.__content
    
    def add_child(self,child_node):
        self.__child_array.append(child_node)

    def get_child_num(self):
        return len(self.__child_array)

    def generate_current_data(self):
        ret = ""
        for item in self.__child_array:
            ret = ret + item.get_content() + self.__separator_between_childs
        return ret
    
    def display_current_node(self):
        if self.__head == NodeType.NORMAL:
            print("normal")
        if self.__head == NodeType.FOR:
            print("for")
        print(self.__content)
        print(len(self.__child_array))
        for item in self.__child_array:
            item.display_current_node()