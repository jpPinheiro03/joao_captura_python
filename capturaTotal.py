import psutil as ps
import pandas as pd
import random
import time
import datetime 
import os


fim = False
contador = 0 
qtdProcess = 0;
qtdNetErrout = 0;

if not os.path.exists("dadosGrupo3Total.csv"):
    df = pd.DataFrame(columns=["user","unidade","timestamp", "cpu", "ram", "disco","qtdPacketLoss","qtdProcessos"])
    df.to_csv("dadosGrupo3Total.csv", index=False, sep=';')

while not fim:
    contador +=1

    qtdProcess = 0;
    qtdNetErrout = 0;

    #dados e tratamento de dados
    user = "Hospital"
    unidade = random.randint(1,3)
    cpuPercent = ps.cpu_percent(interval=1)
    horas = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    memory = ps.virtual_memory().percent
    diskUse = ps.disk_usage('C:\\').percent

    for p in ps.process_iter(attrs=['pid', 'name', 'status']):
        if p.info['status'] == ps.STATUS_RUNNING:
            qtdProcess += 1
    processos = qtdProcess


    dadosNet = ps.net_io_counters(pernic=True)
    for i, stats in dadosNet.items():
        qtdNetErrout += stats.errout

   


    #aplicação de dados
    dados = {
        "user": user,
        "unidade": unidade,
        "timestamp": horas, 
        "cpu": cpuPercent,
        "ram": memory,
        "disco": diskUse,
        "qtdPacketLoss": qtdNetErrout,
        "qtdProcessos": processos
    }

    print(dados)

    df = pd.DataFrame([dados])  
    df.to_csv("dadosGrupo3Total.csv", mode="a", header=False, index=False, sep=';' )

    time.sleep(10)  