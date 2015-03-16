#define SENSOR 18
    #define DISPLAY 7
    void setup() {
        pinMode(RX, INPUT);
        pinMode(DISPLAY, OUTPUT);
    
    }
    
    void loop() {
        digitalWrite(DISPLAY, digitalRead(RX));
    
    }
