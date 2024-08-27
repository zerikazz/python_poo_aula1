from frota import *
import pickle
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
    kms = float(input('Digite com quantos Kms: '))




    print('Cadastre o segundo carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    kms = float(input('Digite com quantos Kms: '))

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, kms, motor = True)
    carro2 = Carro(nm_modelo, nm_marca, nm_cor, kms, motor = True)

    carros = {}
    carros[id(carro1)] = carro1
    carros[id(carro2)] = carro2

    #Negocio do arquivo
    try:
        with open('carros3.plk', 'rb') as arquivo:
            pickle.dump(carros, arquivo)
    except Exception as e:
        print(e)

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
    carro2.desligar()

    print(carro1)
    print(carro2)
    if carro1.get_odometro() >= 600 or carro1.get_tanque() < 0:
        print(f"o carro {carro1.modelo} terminou primeiro o destino/acabou primeiro com a gasolina")
        print(carro1)
    else:
        print(f"o carro {carro2.modelo} terminou primeiro o destino/acabou primeiro com a gasolina")
        print(carro2)
