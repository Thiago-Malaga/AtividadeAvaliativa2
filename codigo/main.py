"""
@file main

Esse arquivo contem testes da implementação da AV2.
A implementação escolhida é Reservar horário de monitoria.
As classes e funcionadlidades são implementadas nos arquivos XXX e YYY e os testes em ZZZ. 
Aqui nesse arquivo só tem os testes básicos do sistema.

---------------------------------------------------------------------------------------------------
| Autores: Gabriel Felipe F. de Souza (2669480) E Thiago André Mattos Málaga (2669641)            |
| Professor: Luiz Antônio Lima                                                                    |
| Data:       19/10/2026                  Ultima modificação: 20/10/2026                          |
| Versão:     1.0                                                                                 |
---------------------------------------------------------------------------------------------------

"""

from datetime import time
from classes import Monitor, Disciplina, Aluno
from servicos import ServicoMonitoria



#TESTES:
monitor = Monitor("Muriel")
disciplina = Disciplina("POO", monitor)
servico = ServicoMonitoria()

horario = disciplina.adicionar_horario(
    "segunda-feira", time(10, 0)
)

horario2 = disciplina.adicionar_horario(
    "segunda-feira", time(11, 0), "grupo", capacidade=10
)

for h in servico.listar_horarios_disponiveis(disciplina):
    print(
        f"{h.dia_semana}: {h.hora_inicio} - {h.hora_fim}"
    )


aluno = Aluno("Bruno", "A123")
reserva = servico.reservar(disciplina, aluno, horario)
reserva = servico.reservar(disciplina, aluno, horario2)

print("Reserva realizada para:", reserva.aluno.nome)
print("Status do horário:", horario.status_reserva)
print("Status do horário2:", horario2.status_reserva, horario2.vagas_disponiveis())
