#Arquivo que omplementa as classes básicas do sistema, sem grandes métodos ou funcionalidades:

#Imports importantes para usar classes de tempo já existentes:
from dataclasses import dataclass, field
from datetime import time

#Esssa classe representa um monitor:
@dataclass
class Monitor:
    nome: str

#Esssa classe representa um aluno:
@dataclass
class Aluno:
    nome: str
    identificador: str

#Esssa classe representa uma reserva, atrelando um horario e um aluno:
#Possui seu tipo de grupo ou individual e vagas
#Também tem métodos para calcular tempo do fim e se ha vagas
@dataclass
class Reserva:
    aluno: Aluno
    horario: "HorarioMonitoria"


#Esssa classe é um horario d monitoria, de 30 min:
@dataclass
class HorarioMonitoria:
    dia_semana: str
    hora_inicio: time
    tipo: str = "individual"
    capacidade: int = 1
    reservas: list = field(default_factory=list)

    @property
    def hora_fim(self):
        minutos = self.hora_inicio.hour * 60 + self.hora_inicio.minute + 30
        return time(minutos // 60, minutos % 60)

    @property
    def status_reserva(self):
        if len(self.reservas) == 0:
            return "livre"
        if len(self.reservas) >= self.capacidade:
            return "lotado"
        return "com vagas"

    def esta_disponivel(self):
        return len(self.reservas) < self.capacidade

    def vagas_disponiveis(self):
        return self.capacidade - len(self.reservas)


#Esssa classe representa uma disciplina atrelada a um mmonitor e uma lista de horarios:
#possui um metodo para colocar horarios na lista e valida-los
@dataclass
class Disciplina:
    nome: str
    monitor: Monitor
    horarios: list = field(default_factory=list)

    def adicionar_horario(
        self, dia_semana, hora_inicio,
        tipo="individual", capacidade=1
    ):
        if tipo not in ("individual", "grupo"):
            raise ValueError("Tipo deve ser individual ou grupo.")

        if tipo == "individual":
            capacidade = 1

        if capacidade < 1:
            raise ValueError("Capacidade inválida.")

        for horario in self.horarios:
            if (
                horario.dia_semana == dia_semana
                and horario.hora_inicio == hora_inicio
            ):
                raise ValueError("Horário já cadastrado.")

        horario = HorarioMonitoria(
            dia_semana, hora_inicio, tipo, capacidade
        )
        self.horarios.append(horario)
        return horario
