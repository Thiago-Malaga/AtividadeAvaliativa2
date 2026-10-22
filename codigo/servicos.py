#Arquivo que implementa os serviços do sistema:

#Import para usar a classe de reserva:
from classes import Reserva

class ServicoMonitoria:
    #Esse metodo lista os horarios disponiveis de uma certa disciplina usando uma varredura na lista dela:
    def listar_horarios_disponiveis(self, disciplina):
        return [
            horario
            for horario in disciplina.horarios
            if horario.esta_disponivel()
        ]

    #Esse horario pega um aluno e uma disciplina e um horario e tenta fazer a reserva se ela ainda permitir ou tiver de fato o horario:
    def reservar(self, disciplina, aluno, horario):
        if horario not in disciplina.horarios:
            raise ValueError("Horário não pertence à disciplina.")

        if not horario.esta_disponivel():
            raise ValueError("Horário sem vagas.")

        for reserva in horario.reservas:
            if reserva.aluno.identificador == aluno.identificador:
                raise ValueError("Aluno já reservou esse horário.")

        reserva = Reserva(aluno, horario)
        horario.reservas.append(reserva)
        return reserva