from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from geopy.geocoders import Nominatim

class FamilyScreen(Screen):
    def __init__(self, **kwargs):
        super(FamilyScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Family Profile'))
        sos_button = Button(text='Send SOS')
        sos_button.bind(on_press=self.send_sos)
        layout.add_widget(sos_button)
        self.add_widget(layout)

    def send_sos(self, instance):
        # Implement SOS functionality
        print("SOS sent!")

class PatientScreen(Screen):
    def __init__(self, **kwargs):
        super(PatientScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Patient Profile'))
        self.add_widget(layout)

class CaretakerScreen(Screen):
    def __init__(self, **kwargs):
        super(CaretakerScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Caretaker Profile'))
        self.add_widget(layout)

class DementiaApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FamilyScreen(name='family'))
        sm.add_widget(PatientScreen(name='patient'))
        sm.add_widget(CaretakerScreen(name='caretaker'))
        return sm

if __name__ == '__main__':
    DementiaApp().run()
