# parâmetros: valores
def many_parameter(*arg):
    print("Was called with ", len(arg), " arguments: ", arg)
    for v in arg:
        print("->", v)

# parâmetros no formato nome=valor
def args_com_nomes_de_parametros(**kwarg):
    print("Was called with ", len(kwarg), " arguments: ", kwarg)
    for k in kwarg:
        print("=>", k, "=", kwarg[k])    

if __name__ == "__main__":
    
    many_parameter()
    many_parameter("Joao")
    many_parameter("Casa 9")
    many_parameter("Joao", "Casa 9")

    args_com_nomes_de_parametros()
    args_com_nomes_de_parametros(nome = "Joao")
    args_com_nomes_de_parametros(endereco = "Casa 9")
    args_com_nomes_de_parametros(endereco = "Casa 9", nome = "Joao")
    args_com_nomes_de_parametros(nome = "Joao", endereco = "Casa 9")