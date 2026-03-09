# EKG-Real-Time-Simulator

Proiectul realizează o simulare avansată a unui semnal electrocardiografic (EKG), transmițând date eșantionate de pe un **Arduino** către o interfață grafică dinamică dezvoltată în **Python**. Este un instrument ideal pentru a înțelege cum funcționează comunicarea serială și monitorizarea semnalelor biologice.

**Caracteristici Principale**
* ** Monitorizare în Timp Real:** Vizualizarea instantanee a semnalului trimis prin protocolul Serial.
* **Grid Medical:** Interfață grafică optimizată cu caroiaj standard (linii la 0.2s și 1.0s) pentru interpretare.
* **Detecție Puls:** LED-ul integrat pe placa Arduino (Pin 13) pulsează sincronizat cu vârful complexului QRS.
* **Parametrizare:** Control precis asupra BPM-ului și a ferestrei de afișare direct din cod.

**Arhitectura Sistemului**
**Hardware**
Codul din `grafic.ino` funcționează ca un generator de funcții specializat:
* **Unda P:** Simulează depolarizarea atrială.
* **Complex QRS:** Recreează vârful înalt al depolarizării ventriculare.
* **Unda T:** Simulează faza de repolarizare.
* **Sincronizare:** Delay-ul este calculat automat pentru a respecta pragul de **100 BPM**.
**Software**
Scriptul `citire_date.py` prelucrează datele brute primite:
* **Biblioteci utilizate:** `pyserial`, `matplotlib`, `drawnow`.
* **Buffer:** Gestionează o fereastră glisantă (rolling window) care afișează ultimele 5 bătăi pentru o cursivitate maximă.
