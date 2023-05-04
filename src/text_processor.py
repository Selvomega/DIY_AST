class TextProcessor:
    __text = ""

    def __init__(self,text=""):
        self.__text = text

    def ReadLines(self):
        buffer = ""
        ret = []
        length = len(self.__text)
        for i in range (0,length):
            buffer = buffer+self.__text[i]
            if self.__text[i] == "\n":
                ret = self.append(ret,buffer)
                buffer = ""
            elif i == length-1:
                ret = self.append(ret,buffer)
        return ret
    
    def ReadLinesExcludeEmpty(self):
        buffer = ""
        ret = []
        length = len(self.__text)
        for i in range (0,length):
            buffer = buffer+self.__text[i]
            if self.__text[i] == "\n" :
                ret = self.append_exclude_empty_line(ret,buffer)
                buffer = ""
            elif i == length-1:
                ret = self.append_exclude_empty_line(ret,buffer)
        return ret
    
    def DivideByBlock(self):
        block_buffer = ""
        line_buffer = ""
        prefetch_line_buffer = ""
        ret = []
        lines = self.ReadLinesExcludeEmpty()
        if len(lines)==0:
            raise ValueError("Empty file?!")
        tab_num = self.CountPrevTab(lines[0])
        length = len(lines)
        for i in range(0, length):
            line_buffer = lines[i]
            if self.CountPrevTab(line_buffer)<tab_num:
                raise ValueError("Invalid file format?!")
            if i==length-1:
                block_buffer = block_buffer+line_buffer
                ret = self.append(ret,block_buffer)
            else:
                prefetch_line_buffer = lines[i+1]
                if self.CountPrevTab(line_buffer) == tab_num and self.CountPrevTab(prefetch_line_buffer) > tab_num:
                    if len(block_buffer) != 0:
                        ret = self.append(ret,block_buffer)
                    block_buffer = line_buffer
                elif self.CountPrevTab(line_buffer) > tab_num and self.CountPrevTab(prefetch_line_buffer) == tab_num:
                    block_buffer = block_buffer+line_buffer
                    ret = self.append(ret,block_buffer)
                    block_buffer = ""
                else:
                    block_buffer = block_buffer+line_buffer
        return ret
    
    def CountPrevTab(self,input):
        length = len(input)
        counter = 0
        for i in range (0, length):
            if input[i] == " ":
                counter = counter + 1
                if i==length-1 and counter%4 != 0:
                    raise ValueError("The input is not the correct format?!")
            else:
                if counter%4 != 0:
                    raise ValueError("The input is not the correct format?!")
                break
        num = counter//4
        return num
    
    def RemovePrevTab(self,input):
        length = len(input)
        counter = 0
        ret  = ""
        if not self.check_prev_tab(input):
            raise ValueError("The input is not the correct format?!")
        for i in range (0, length):
            if input[i] == " ":
                counter = counter + 1
            else:
                break
        for i in range(counter,length):
            ret = ret+input[i]
        return ret
    
    def check_empty_line(self,input):
        length = len(input)
        for i in range(0,length):
            if i == length-1:
                if input[i] != "\n" and input[i] != " ":
                    return False
            else:
                if input[i] != " ":
                    return False
        return True

    def check_prev_tab(self,input):
        length = len(input)
        counter = 0
        for i in range (0, length):
            if input[i] == " ":
                counter = counter + 1
                if i==length-1 and counter%4 != 0:
                    return False
            else:
                if counter%4 != 0:
                    return False
                break
        return True
    
    def append(self,array,content):
        if self.check_prev_tab(content):
            array.append(content)
        else:
            raise ValueError("The input is not the correct format?!")
        return array
    
    def append_exclude_empty_line(self,array,content):
        if self.check_prev_tab(content):
            if not self.check_empty_line(content):
                array.append(content)
        else:
            raise ValueError("The input is not the correct format?!")
        return array
    
