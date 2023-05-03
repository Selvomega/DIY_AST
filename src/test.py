from text_processor import TextProcessor

with open("block_test","r") as handle:
    data = handle.read()

processor = TextProcessor(data)
blocks = processor.DivideByBlock()
for i in range(0,len(blocks)):
    print(i)
    print(blocks[i])