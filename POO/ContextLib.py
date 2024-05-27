from contextlib import contextmanager

@contextmanager
def my_open(path_,mode):
    try:
        print("Abrindo arquivo")
        arq = open(path_, mode, encoding='utf8')
        yield arq
    except Exception as exe:
        print(exe)
    finally:
        print("Fechando arquivo")
        arq.close()

with my_open ('arquivo.txt', 'w') as arq:
    arq.write("---", 123)