import os
import sys
def order_by_size(file_list):
    def fsize(f):
        return os.stat(f).st_size
    file_list.sort(key=fsize)
    files=file_list[-5:]
    return files
def list_of_file(d):
    files=[]
    for i in os.listdir(d):
        file_name=os.path.join(d,i)
        if os.path.isfile(file_name):
            files.append(file_name)

    return files
if __name__ == "__main__":
    l=list_of_file(sys.argv[1])
    
    n= order_by_size(l)
    print(n)
  
