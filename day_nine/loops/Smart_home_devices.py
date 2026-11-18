#12. Smart Home Devices (Multiple Inheritance)
#A smart home device may have both WiFi connectivity and Voice control features.
#Create classes WiFiDevice and VoiceAssistant, and a class SmartSpeaker that inherits from both using multiple inheritance.


class WiFiDevice:
    def connect_wifi(self):
        print("Connected to WiFi")


class VoiceAssistant:
    def use_voice_control(self):
        print("Voice control is ready")


class SmartSpeaker(WiFiDevice, VoiceAssistant):
    pass


speaker = SmartSpeaker()
speaker.connect_wifi()
speaker.use_voice_control()
