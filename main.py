import uuid
from datetime import datetime

class Cliente:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.id = str(uuid.uuid4())  # ID único para cada cliente


class Quarto:
    def __init__(self, numero, tipo, preco_diaria):
        self.numero = numero
        self.tipo = tipo  # Pode ser 'single', 'double' ou 'suite'
        self.preco_diaria = preco_diaria
        self.disponivel = True  # Status de disponibilidade (True = disponível, False = ocupado)


class Reserva:
    def __init__(self, cliente, quarto, data_check_in, data_check_out):
        self.dono_reserva = cliente
        self.quarto_reservado = quarto
        self.data_check_in = data_check_in
        self.data_check_out = data_check_out
        self.status_reserva = "Confirmada"  # Status inicial da reserva

    def cancelar_reserva(self):
        self.status_reserva = "Cancelada"
        self.quarto_reservado.disponivel = True  # O quarto volta a ficar disponível


class GerenciadorDeReservas:
    def __init__(self):
        self.quartos = []  # Lista de quartos disponíveis
        self.reservas = []  # Lista de reservas feitas

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)

    def verificar_disponibilidade(self, quarto):
        return quarto.disponivel

    def criar_reserva(self, cliente, quarto, data_check_in, data_check_out):
        if self.verificar_disponibilidade(quarto):
            nova_reserva = Reserva(cliente, quarto, data_check_in, data_check_out)
            quarto.disponivel = False  # O quarto fica ocupado após a reserva
            self.reservas.append(nova_reserva)
            return nova_reserva
        else:
            print(f"O quarto {quarto.numero} não está disponível.")
            return None

    def modificar_reserva(self, reserva, novo_quarto, nova_data_check_in, nova_data_check_out):
        if self.verificar_disponibilidade(novo_quarto):
            reserva.quarto_reservado.disponivel = True  # Libera o quarto antigo
            reserva.quarto_reservado = novo_quarto
            reserva.data_check_in = nova_data_check_in
            reserva.data_check_out = nova_data_check_out
            novo_quarto.disponivel = False  # Marca o novo quarto como reservado
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


# Exemplo de uso:

# Criando instâncias de clientes e quartos
cliente1 = Cliente("João Silva", "1234-5678", "joao@exemplo.com")
cliente2 = Cliente("Maria Oliveira", "9876-5432", "maria@exemplo.com")

quarto1 = Quarto(101, "single", 150.00)
quarto2 = Quarto(102, "double", 250.00)
quarto3 = Quarto(103, "suite", 500.00)

# Criando o gerenciador de reservas
gerenciador = GerenciadorDeReservas()

# Adicionando quartos ao sistema
gerenciador.adicionar_quarto(quarto1)
gerenciador.adicionar_quarto(quarto2)
gerenciador.adicionar_quarto(quarto3)

# Criando reservas
reserva1 = gerenciador.criar_reserva(cliente1, quarto1, datetime(2025, 4, 10), datetime(2025, 4, 15))
reserva2 = gerenciador.criar_reserva(cliente2, quarto2, datetime(2025, 4, 12), datetime(2025, 4, 18))

# Listando reservas
gerenciador.listar_reservas()

# Modificando uma reserva
reserva_modificada = gerenciador.modificar_reserva(reserva1, quarto3, datetime(2025, 4, 14), datetime(2025, 4, 20))

# Cancelando uma reserva
gerenciador.cancelar_reserva(reserva2)

# Listando as reservas após a modificação e cancelamento
gerenciador.listar_reservas()
