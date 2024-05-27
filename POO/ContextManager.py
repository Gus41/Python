class OpenArq:

  def __init__(self,path,module) -> None:
    self._path = path
    self._module = module
    self._arq = None
    print("init")
    
  def __enter__(self):
    print("Entering")
    self._arq = open(self._path,self._module)
    return self._arq
    
  def __exit__(self, exc_type, exc_val, exc_tb):
    self._arq.close()
    print("Exiting")

openArq = OpenArq("arq.txt",'w')

with openArq as arq:
  arq.write("Arq")
  print("Context: ", arq)