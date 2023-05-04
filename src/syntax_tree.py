from node import Node
from node_type import NodeType
from text_processor import TextProcessor

class SyntaxTree:

    def __init__(self):
        self.__buffer = ""
        self.__root = Node()
        self.__for_reserved = "the content of a for-loop\n"
        self.__tab_reserved = "    "

    def build_tree(self,text):
        self.__root = self.build_sub_tree(self.__root,text)

    def build_sub_tree(self,node:Node,text)->Node:
        ret_node = node
        processor = TextProcessor(text)
        blocks = processor.DivideByBlock()
        for single_block in blocks:
            node_type = self.recognize_pattern(single_block)
            if node_type == NodeType.NORMAL:
                new_node = Node(NodeType.NORMAL,single_block)
                ret_node.add_child(new_node)
            if node_type == NodeType.FOR:
                for_placeholder = self.generate_for_placeholder(single_block)
                for_content = self.process_for_content(single_block)
                new_node = Node(NodeType.FOR,for_placeholder)
                new_node = self.build_sub_tree(new_node,for_content)
                ret_node.add_child(new_node)
        return ret_node

    def scan_tree(self):
        # TODO 
        pass

    def print_tree(self):
        self.__root.display_current_node()

    def recognize_pattern(self,text):
        processor = TextProcessor()
        processed_text = processor.RemovePrevTab(text)
        if len(processed_text)<3:
            return NodeType.NORMAL
        if processed_text[0:3] == "for":
            return NodeType.FOR
        return NodeType.NORMAL
    
    def generate_for_placeholder(self,block):
        processor = TextProcessor()
        tab_num = processor.CountPrevTab(block)+1
        for_placeholder = self.__tab_reserved*tab_num+self.__for_reserved
        return for_placeholder
    
    def process_for_content(self,block) -> str:
        length = len(block)
        for i in range(0,length):
            if block[i]=="\n": 
                return block[i+1:length]
        return ""