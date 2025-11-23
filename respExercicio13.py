class Veiculo:
    def __init__(self, vel_max):
        self.velocidade = 0
        self.vel_max = vel_max

    def acelerar(self, valor):
        nova_vel = self.velocidade + valor
        self.velocidade = min(nova_vel, self.vel_max)

    def frear(self, valor):
        nova_vel = self.velocidade - valor
        self.velocidade = max(nova_vel, 0)

    def get_velocidade(self):
        return self.velocidade


class Carro(Veiculo):
    def __init__(self):
        super().__init__(vel_max=180)


class Bicicleta(Veiculo):
    def __init__(self):
        super().__init__(vel_max=50)


class Aviao(Veiculo):
    def __init__(self):
        super().__init__(vel_max=900)


class ControladorTrafego:
    def controlar(self, veiculo: Veiculo):
        veiculo.acelerar(30)
        veiculo.frear(10)
        return veiculo.get_velocidade()
   

def testar_veiculo(veiculo):
    print(f"Testando {type(veiculo).__name__}")
    veiculo.acelerar(30)
    veiculo.acelerar(20)
    print(f"Velocidade: {veiculo.get_velocidade()} km/h")
    veiculo.frear(10)
    print(f"Velocidade após frear: {veiculo.get_velocidade()} km/h")

# Todos os veículos devem funcionar da mesma forma
carro = Carro()
bicicleta = Bicicleta()
aviao = Aviao()

testar_veiculo(carro)
testar_veiculo(bicicleta)
testar_veiculo(aviao)