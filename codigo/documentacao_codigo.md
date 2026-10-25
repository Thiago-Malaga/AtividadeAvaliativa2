Sistema de Agendamento de Monitoria (AV2)

Documentação do sistema de agendamento e reserva de horários de monitoria desenvolvido em Python.

-> Autores:

Gabriel Felipe F. de Souza (RA: 2669480)

Thiago André Mattos Málaga (RA: 2669641)

Professor: Luiz Antônio Lima

-> Visão Geral:

Este projeto foi criado para gerenciar o agendamento de sessões de monitoria acadêmica. O sistema permite cadastrar disciplinas, associar monitores, definir horários de atendimento (individuais ou em grupo) e gerenciar as reservas realizadas pelos alunos com validações automáticas de vagas e sobreposição.

-> Estrutura de Arquivos:

classes.py: Contém a definição das entidades do sistema (Monitor, Aluno, Reserva, HorarioMonitoria e Disciplina).

servicos.py: Contém a classe ServicoMonitoria, responsável pelas regras de negócio (listagem de horários disponíveis e realização de reservas).

main.py: Arquivo principal com um script de demonstração e testes manuais básicos do fluxo do sistema.

testesgreen.py: Suíte de testes unitários automatizados utilizando a bib unittest para garantir que as validações funcionem corretamente.

-> Classes e Entidades Principal (classes.py / servicos.py)

Monitor: Representa o tutor/monitor responsável por uma disciplina (possui nome).

Aluno: Representa o aluno interessado nas monitorias (possui nome e identificador/RA).

HorarioMonitoria: Representa a sessão de monitoria (duração fixa de 30 min). Pode ser do tipo individual (1 vaga) ou grupo (capacidade definida). Possui propriedades para verificar status_reserva, esta_disponivel() e vagas_disponiveis().

Disciplina: Atrela um Monitor a uma lista de HorarioMonitoria. Possui o método adicionar_horario() que valida duplicidades e limites de capacidade.

Reserva: Associa um Aluno a um HorarioMonitoria.

ServicoMonitoria: Centraliza as operações do sistema:

listar_horarios_disponiveis(disciplina): Retorna os horários com vagas abertas.

reservar(disciplina, aluno, horario): Realiza a reserva validando disponibilidade e impedindo que o mesmo aluno se inscreva duas vezes no mesmo horário.

-> Como Executar

O projeto utiliza apenas a biblioteca padrão do Python não sendo necessária a instalação de dependências externas.

1. Executar a demonstração principal (main.py)

Para rodar a simulação e ver o funcionamento básico no terminal:

python main.py


2. Executar os Testes Automatizados (testesgreen.py)

Para rodar todos os testes unitários e verificar o correto funcionamento das regras do sistema:

python -m unittest -v testesgreen.py