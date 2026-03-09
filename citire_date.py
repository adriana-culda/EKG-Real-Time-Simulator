import serial
import matplotlib.pyplot as plt
from drawnow import drawnow

#conexiune seriala
serialArduino = serial.Serial("COM6", 9600)
valori = []

#sincronizate cu arduino
bpm = 100
numar_valori_pe_bataie = 35
delay_per_punct_ms = 60000 / (bpm * numar_valori_pe_bataie)  # ms între puncte
frecventa= 1000 / delay_per_punct_ms  # Hz

numar_batai = 5
dimensiune_fereastra = int(numar_valori_pe_bataie * numar_batai)  #valori arduino * batai

# valori medii
valori = [512] * dimensiune_fereastra

def plotare():
    plt.clf() #redesenare 
    durata = len(valori) / frecventa
    timp = [i / frecventa for i in range(len(valori))]
    plt.plot(timp, valori, "b-", label="Semnal EKG")
    plt.xlabel("Timp (secunde)")
    plt.ylabel("Tensiune (unități ADC)")  #Analog to Digital Converter
    plt.title(f"Simulare semnal EKG ({bpm} bpm)")
    plt.ylim(400, 900)
    plt.xlim(0, durata)
    plt.grid(True, c='r')

    #linii verticale 
    for t in range(int(durata / 0.2) + 1):
        plt.axvline(x=t * 0.2, color='gray', linestyle='--', linewidth=0.4)
    for t in range(int(durata) + 1):
        plt.axvline(x=t, color='gray', linestyle='-', linewidth=1.2)
        
    plt.legend()

#afisare timp real
plt.ion()
fig = plt.figure()
k = 0
while True:
    if serialArduino.in_waiting:
        x = serialArduino.readline().decode("utf8").strip()
        try:
            valoare = int(x)
            valori.append(valoare)
            if len(valori) > dimensiune_fereastra:
                valori.pop(0)
            k += 1
            drawnow(plotare) 
            if k > dimensiune_fereastra:
                serialArduino.close()
                break
        except ValueError: 
            pass