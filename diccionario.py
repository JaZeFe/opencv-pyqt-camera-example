import sys, itertools

def tuple_to_string(temp_tuple):
    string = ""
    for char in temp_tuple:
        string += char
    return string 

def main():
    if len(sys.argv) > 1:
        diccionario = "abcdefghijkpqrstumnowxyz"

        n = int(sys.argv[1])
        for i in range(1, n+1):
            input_param = [diccionario]*i
            for t in itertools.product(*input_param):
                print tuple_to_string(t), 
    else:
        print "Error debes darle n de entrada, diccionario.py longitud_maxima, ejemplo: python diccionario.py 3"
main()
