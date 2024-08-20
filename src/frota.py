class Carro:
    modelo : str
    marca : str
    cor : str
    __odometro = 0.0
    __motor_on = False
    tanque = 0.0
    consumo_medio = 0.0
    kms = 0.0

    def __init__(self, modelo : str, marca : str, cor : str,
                       odometro : float, motor : bool, tanque : float , consumo_medio : float, kms : float):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.__odometro = odometro
        self.__motor_on = motor
        self.tanque = tanque
        self.consumo_medio = consumo_medio
        self.kms = kms

    def ligar(self):
        if not self.__motor_on:
            self.__motor_on = True
        else:
            raise Exception("Erro: Motor já ligado!")

    def acelerar(self, velocidade : float, tempo : float):
        if self.__motor_on:
            self.__odometro += velocidade * tempo
        else:
            raise Exception("Erro: Não é possível acelerar! Motor desligado!")

        if self.__motor_on and self.tanque > 0 :
            km = velocidade * tempo
            litros = km / self.consumo_medio
            if self.tanque >= litros:
                self.__odometro += km
                self.tanque -= litros
        else:
            km = self.tanque * self.consumo_medio
            self.__odometro += km
            self.tanque = 0

    def desligar(self):
        if self.__motor_on:
            self.__motor_on = False
        else:
            raise Exception("Erro: Motor já desligado!")

    def __str__(self):
        info = (f'Carro {self.modelo}, marca {self.marca}, '
                f'cor {self.cor}\n{self.__odometro} Km, '
                f'motor {self.__motor_on}')
        return info





