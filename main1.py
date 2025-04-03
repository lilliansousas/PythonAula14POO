import uuid
from datetime import datetime

class Cliente:
    def __init__(self, nome, telefone, email, id_unico):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.id_unico = id_unico

class Quarto:
    def __init__(self, numero, tipo, preço_diaria):
        self.numero = numero
        self.tipo = tipo
        self.preço = preço_diaria
        self.disponivel = True

class Reserva:
    def __init__(self, dono_da_reserva, quarto_reservado, data_check_in, data_check_out, status_da_reserva):
        self.dono_da_reserva = dono_da_reserva
        self.quarto_reservado = quarto_reservado
        self.data_check_in = data_check_in
        self.data_check_out = data_check_out
        self.status_reserva = "CONFIRMADA"

    def reserva_cancelada(self):
        self.status_reserva = "CANCELADA"
        self.quarto_reservado.disponivel = True


class GerenciadorDeReservas:
    def __init__(self):
        self.quartos = []  
        self.reservas = [] 

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)

    def verificar_disponibilidade(self, quarto):
        return quarto.disponivel

    def criar_reserva(self, cliente, quarto, data_check_in, data_check_out):
        if self.verificar_disponibilidade(quarto):
            nova_reserva = Reserva(cliente, quarto, data_check_in, data_check_out)
            quarto.disponivel = False  
            self.reservas.append(nova_reserva)
            return nova_reserva
        else:
            print(f"O quarto {quarto.numero} não está disponível.")
            return None

    def modificar_reserva(self, reserva, novo_quarto, nova_data_check_in, nova_data_check_out):
        if self.verificar_disponibilidade(novo_quarto):
            reserva.quarto_reservado.disponivel = True  
            reserva.quarto_reservado = novo_quarto
            reserva.data_check_in = nova_data_check_in
            reserva.data_check_out = nova_data_check_out
            novo_quarto.disponivel = False  
            reserva.status_reserva = "Modificada"
            return reserva
        else:
            print(f"O novo quarto {novo_quarto.numero} não está disponível.")
            return None

    def cancelar_reserva(self, reserva):
        reserva.cancelar_reserva()
        print(f"A reserva de {reserva.dono_reserva.nome} foi cancelada.")

    def listar_reservas(self):
        for reserva in self.reservas:
            print(f"Reserva: {reserva.dono_reserva.nome}, Quarto: {reserva.quarto_reservado.numero}, "
                f"Check-in: {reserva.data_check_in}, Check-out: {reserva.data_check_out}, Status: {reserva.status_reserva}")


cliente1 = Cliente("João Silva", "1234-5678", "joao@exemplo.com")
cliente2 = Cliente("Maria Oliveira", "9876-5432", "maria@exemplo.com")

quarto1 = Quarto(101, "single", 150.00)
quarto2 = Quarto(102, "double", 250.00)
quarto3 = Quarto(103, "suite", 500.00)

gerenciador = GerenciadorDeReservas()

gerenciador.adicionar_quarto(quarto1)
gerenciador.adicionar_quarto(quarto2)
gerenciador.adicionar_quarto(quarto3)

reserva1 = gerenciador.criar_reserva(cliente1, quarto1, datetime(2025, 4, 10), datetime(2025, 4, 15))
reserva2 = gerenciador.criar_reserva(cliente2, quarto2, datetime(2025, 4, 12), datetime(2025, 4, 18))

gerenciador.listar_reservas()

reserva_modificada = gerenciador.modificar_reserva(reserva1, quarto3, datetime(2025, 4, 14), datetime(2025, 4, 20))

gerenciador.cancelar_reserva(reserva2)

gerenciador.listar_reservas()            
