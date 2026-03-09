const uint16_t ekgData[] = {    //amplitudine 512=0V
  // Linie bazală + val P - depolarizare atriala
  512, 512, 514, 522, 516, 514, 512, 512, 
  // Complex QRS - depolarizare ventriculara 
  500, 550, 650, 712, 600, 520, 437,
  // Val T - repolarizarea ventriculara
  512, 512, 514, 518, 522, 552, 522, 518, 514,
  //pauza intre batai
  512, 512, 512, 512, 512 
  //30 puncte
};


constexpr size_t lungime = sizeof(ekgData) / sizeof(ekgData[0]); //calc. la comp
size_t index = 0;
const int ledPin = 13; 
const int prag = 700; // Prag pentru detectare vârf R
const int bpm=100;
void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  if (Serial) {
    int value = ekgData[index];
    Serial.println(value);
    
    if (value >= prag) {
      digitalWrite(ledPin, HIGH);
      delay(100);
    } else {
      digitalWrite(ledPin, LOW);
    }
    index = (index + 1) % lungime; //asigura reluarea datelor
    int durata_bataie = 60000 / bpm; // ms per ciclu
    int delay_per_punct = durata_bataie / lungime; //durata / puncte
  delay(delay_per_punct);
  }
}
