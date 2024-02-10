import time

class Time: #TEAM OBJECTS
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0
        self.gols = 0
        self.gols_sofridos = 0
        self.saldo = 0

def tabela(lista_times): #SHOW TABLE IN THE TERMINAL
    lista_times = sorted(lista_times, key=lambda x: (x.pontos, x.saldo, x.gols), reverse=True)
    print("{:<5} {:<15} {:<10} {:<10} {:<15} {:<5}".format("#", "Time", "Pontos", "Gols", "Gols Sofridos", "SG"))
    i = 1
    for time in lista_times:
        print("{:<5} {:<15} {:<10} {:<10} {:<15} {:<5}".format(i, time.nome, time.pontos, time.gols, time.gols_sofridos, time.saldo))
        i += 1

def jogo(casa, fora): #GAMES
    print(f"{casa.nome} X {fora.nome}")
    time.sleep(0.8)
    casa_gols = input(f"{casa.nome}: ")
    time.sleep(0.1)
    fora_gols = input(f"{fora.nome}: ")
    try:
        casa_gols = int(casa_gols)
        fora_gols = int(fora_gols)
    except ValueError:
        print("Apenas números são válidos.")
    if casa_gols > fora_gols:
        casa.pontos += 3
    elif casa_gols < fora_gols:
        fora.pontos += 3
    else:
        casa.pontos += 1
        fora.pontos += 1
    casa.gols += casa_gols
    fora.gols += fora_gols
    casa.gols_sofridos += fora_gols
    fora.gols_sofridos += casa_gols
    casa.saldo = casa.gols - casa.gols_sofridos
    fora.saldo = fora.gols - fora.gols_sofridos


print('-----BEM-VINDO AO SIMULATOR-----')
time_1 = Time(input("Nome da 1ª equipe: "))
time_2 = Time(input("Nome da 2ª equipe: "))
time_3 = Time(input("Nome da 3ª equipe: "))
time_4 = Time(input("Nome da 4ª equipe: "))
time_5 = Time(input("Nome da 5ª equipe: "))
time_6 = Time(input("Nome da 6ª equipe: "))
time_7 = Time(input("Nome da 7ª equipe: "))
time_8 = Time(input("Nome da 8ª equipe: "))

print("-----1ª RODADA DO CAMPEONATO!-----")
time.sleep(1)
jogo(time_1, time_2)
jogo(time_3, time_4)
jogo(time_5, time_6)
jogo(time_7, time_8)
equipes = [time_1, time_2, time_3, time_4, time_5, time_6, time_7, time_8]
time.sleep(1)
tabela(equipes)
time.sleep(0.5)
print("-----2ª RODADA DO CAMPEONATO!-----")
jogo(time_2, time_3)
jogo(time_4, time_1)
jogo(time_6, time_7)
jogo(time_8, time_5)
time.sleep(1)
tabela(equipes)
time.sleep(0.5)
print("-----3ª RODADA DO CAMPEONATO!-----")
jogo(time_1, time_3)
jogo(time_2, time_4)
jogo(time_5, time_7)
jogo(time_6, time_8)
time.sleep(1)
tabela(equipes)
time.sleep(0.5)
print("-----4ª RODADA DO CAMPEONATO!-----")
jogo(time_8, time_1)
jogo(time_7, time_2)
jogo(time_6, time_3)
jogo(time_5, time_4)
time.sleep(1)
tabela(equipes)
time.sleep(0.5)
print("-----5ª RODADA DO CAMPEONATO!-----")
jogo(time_1, time_7)
jogo(time_2, time_8)
jogo(time_3, time_5)
jogo(time_4, time_6)
time.sleep(1)
tabela(equipes)
time.sleep(0.5)
print("-----6ª RODADA DO CAMPEONATO!-----")
jogo(time_2, time_6)
jogo(time_5, time_1)
jogo(time_3, time_8)
jogo(time_4, time_7)
time.sleep(1)
tabela(equipes)
time.sleep(0.5)
print("-----7ª RODADA DO CAMPEONATO!-----")
jogo(time_8, time_4)
jogo(time_7, time_3)
jogo(time_6, time_1)
jogo(time_5, time_2)
time.sleep(0.4)
print("-----CLASSIFICAÇÃO FINAL-----")
time.sleep(0.2)
tabela(equipes)
time.sleep(0.5)


