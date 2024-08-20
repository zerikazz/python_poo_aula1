from frota import *
def operar_carro (carro : Carro):
    print('1- Ligar motor')
    print('2- Desligar motor')
    print('3- Acelerar')

    op = 0
    while op not in (1, 2, 3):
        op = int(input("Digite as opcoes[1-3]: "))

    if op == 1:
        carro1.ligar()
    elif op == 2:
        carro1.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo: "))
        carro1.acelerar(v, t)

if __name__ == "__main__":
    print('Cadastre o primeiro carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    litros = input('Digite quantos litros tem no tanque')
    consumo_medio = input('Digite o consumo medio de litros do carro por km')

    kms = float(input('Digite com quantos Kms: '))

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, 0, False, litros, consumo_medio)

    print('Cadastre o segundo carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    litros = input('Digite quantos litros tem no tanque')
    consumo_medio = input('Digite o consumo medio de litros do carro por km')

    carro2 = Carro(nm_modelo, nm_marca, nm_cor, 0, False, litros, consumo_medio)
    '''
    Controlando o carro 
    '''
    while (carro1.odometro < 300 and carro2.odometro < 300) and (carro1.litros > 0 or carro2.litros > 0):
        try:
            op = 0
            while op not in (1,2):
                op = int(input("Qual carro [1,2]? "))

                if op == 1:
                    operar_carro(carro1)
                if op == 2:
                    operar_carro(carro2)
                else:
                    print('Numeros invalidos')

            print('Infos atuais do carro')
            print(carro1)
        except Exception as e:
            print("Erro!")
            print(e)

    carro1.desligar()
    print(carro1)
    print('Parou')

    carro2.desligar()
    print(carro2)
    print('Parou')

