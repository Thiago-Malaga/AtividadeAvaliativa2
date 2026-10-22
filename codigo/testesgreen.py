import unittest
from datetime import time
from classes import Monitor, Disciplina, Aluno
from servicos import ServicoMonitoria


class TestMonitoria(unittest.TestCase):

    def setUp(self):
        # definicao de monitores
        self.monitor_fisica = Monitor("Rodolfo")
        self.monitor_calculo = Monitor("Hiran")
        self.monitor_poo = Monitor("Tamara")

        # definicao de disciplinas
        self.fisica = Disciplina(
            "fisica",
            self.monitor_fisica
        )

        self.calculo = Disciplina(
            "Cálculo",
            self.monitor_calculo
        )

        self.poo = Disciplina(
            "POO",
            self.monitor_poo
        )

        # definicao de servico
        self.servico = ServicoMonitoria()

        # horarios para teste
        self.horario_fisica = self.fisica.adicionar_horario(
            "segunda-feira",
            time(10, 0)
        )

        self.horario_calculo = self.calculo.adicionar_horario(
            "terça-feira",
            time(14, 0)
        )

        self.horario_poo = self.poo.adicionar_horario(
            "quarta-feira",
            time(16, 0)
        )

        # Alunos
        self.Gabriel = Aluno("Gabriel", "a2669480")
        self.GustavoF = Aluno("GustavoF", "a2669510")
        self.GustavoH = Aluno("GustavoH", "a2669528")


#testes que sao pra dar certo

#testes de horario
    def test_horario_tem_30_minutos(self):
        self.assertEqual( self.horario_fisica.hora_fim, time(10, 30))

    def test_listar_horarios_disponiveis(self):
        horarios = self.servico.listar_horarios_disponiveis(self.fisica)
        self.assertIn(self.horario_fisica, horarios)

    def test_impedir_reserva_em_horario_lotado(self):
        self.servico.reservar( self.fisica, self.Gabriel,self.horario_fisica)

        with self.assertRaises(ValueError):
            self.servico.reservar(self.fisica, self.GustavoF, self.horario_fisica)

    def test_impedir_horario_duplicado(self):
        with self.assertRaises(ValueError):
            self.fisica.adicionar_horario("segunda-feira", time(10, 0))

    def test_listar_horarios_nao_mostra_horario_lotado(self):
        self.servico.reservar(self.fisica, self.Gabriel, self.horario_fisica)

        horarios = self.servico.listar_horarios_disponiveis(self.fisica)
        self.assertNotIn(self.horario_fisica, horarios)

    def test_permitir_varios_alunos_em_horario_de_grupo(self):
        grupo = self.poo.adicionar_horario("quinta-feira", time(14, 0), tipo="grupo",capacidade=3)

        self.servico.reservar(self.poo, self.Gabriel, grupo)
        self.servico.reservar( self.poo, self.GustavoF, grupo)
        self.assertEqual(len(grupo.reservas), 2)
#fim testes de horaria

#testes de reserva

    #uma pra cada materia cadastrada
    def test_reserva_fisica(self):
        reserva = self.servico.reservar(self.fisica, self.Gabriel, self.horario_fisica)

        self.assertEqual( reserva.aluno.nome, "Gabriel")
        self.assertEqual(self.horario_fisica.status_reserva, "lotado")

    def test_reserva_calculo(self):
        reserva = self.servico.reservar(self.calculo, self.GustavoF, self.horario_calculo)

        self.assertEqual(reserva.aluno.nome, "GustavoF")
        self.assertEqual(self.horario_calculo.status_reserva, "lotado")

    def test_reserva_poo(self):
        reserva = self.servico.reservar(self.poo, self.GustavoH, self.horario_poo)

        self.assertEqual(reserva.aluno.nome, "GustavoH")
        self.assertEqual(self.horario_poo.status_reserva, "lotado")


    def test_impedir_reserva_horario_de_outra_disciplina(self):
        with self.assertRaises(ValueError):
            self.servico.reservar(self.fisica, self.Gabriel, self.horario_calculo)

    def test_impedir_aluno_reservar_duas_vezes(self):
        self.servico.reservar(self.fisica, self.Gabriel, self.horario_fisica)

        with self.assertRaises(ValueError):
            self.servico.reservar(self.fisica, self.Gabriel, self.horario_fisica)

    #reserva em grup
    def test_reserva_em_grupo(self):
        grupo = self.poo.adicionar_horario("quinta-feira", time(14, 0), tipo="grupo", capacidade=2)

        self.servico.reservar(self.poo, self.Gabriel, grupo)
        self.servico.reservar(self.poo, self.GustavoF, grupo)

        self.assertEqual(grupo.status_reserva,"lotado")

    def test_impedir_reserva_quando_grupo_atingir_capacidade(self):
        grupo = self.poo.adicionar_horario("quinta-feira", time(14, 0), tipo="grupo", capacidade=2)

        self.servico.reservar(self.poo, self.Gabriel, grupo)
        self.servico.reservar(self.poo, self.GustavoF, grupo)

        with self.assertRaises(ValueError):
            self.servico.reservar(self.poo, self.GustavoH, grupo)
#fim testes de reserva


if __name__ == "__main__":
    unittest.main()