import os 

class read_tle : 
    
    def encode(self, path):
        output = []
        with open(path) as fp:
            for line in fp:
                li = line.split(' ')
                li = '/'.join(li)
                li = li.replace('\n', '')
                output.append(li)
        return ('%'.join(output))

    def decode(self, tle):
        output = []
        tle = tle.split('%') 
        for column in tle: 
            column = column.replace('/', ' ')
            output.append(column) 

        return output

if __name__=="__main__":
    rt = read_tle() 
    print(rt.encode("../tlenew.txt"))

