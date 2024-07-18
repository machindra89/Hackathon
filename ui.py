from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from geopy.geocoders import Nominatim
import requests

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
        data = {'message': 'SOS from Family'}
        response = requests.post('http://127.0.0.1:5000/send_sos', json=data)
        print(response.json())

class PatientScreen(Screen):
    def __init__(self, **kwargs):
        super(PatientScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Patient Profile'))
        location_button = Button(text='Get Location')
        location_button.bind(on_press=self.get_location)
        layout.add_widget(location_button)
        self.add_widget(layout)

    def get_location(self, instance):
        geolocator = Nominatim(user_agent="dementia_app")
        location = geolocator.geocode("Your Address Here")
        print(f"Location: {location.latitude}, {location.longitude}")

class CaretakerScreen(Screen):
    def __init__(self, **kwargs):
        super(CaretakerScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Caretaker Profile'))
        sos_button = Button(text='Check SOS Alerts')
        sos_button.bind(on_press=self.check_sos)
        layout.add_widget(sos_button)
        self.add_widget(layout)

    def check_sos(self, instance):
        response = requests.get('http://127.0.0.1:5000/get_sos')
        alerts = response.json().get('alerts', [])
        for alert in alerts:
            print(alert)

class DementiaApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FamilyScreen(name='family'))
        sm.add_widget(PatientScreen(name='patient'))
        sm.add_widget(CaretakerScreen(name='caretaker'))
        return sm

if __name__ == '__main__':
    DementiaApp().run()
