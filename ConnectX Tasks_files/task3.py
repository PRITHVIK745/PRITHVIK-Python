class Device:
    def __init__(self, brand):
        self.brand=brand

class VoiceControl(Device):
    def __init__(self,brand):
        super().__init__(brand)
    def voice_activate(self):
        pass

class AppControl(Device):
    def app_activate(self):
        pass

class SmartSpeaker(VoiceControl, AppControl):
    
    def control_methods(self):
        return f"{self.brand} can be controlled via voice and app." 

s1 = SmartSpeaker("Echo")
print( s1.control_methods())