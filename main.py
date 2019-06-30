from kivy.app import App
from kivy.uix.label import Label
from jnius import autoclass

DisplayMetrics = autoclass('android.util.DisplayMetrics')
metrics = DisplayMetrics()

class MyApp(App):

    def build(self):
        return Label(text=str(metrics.getDeviceDensity()))

if __name__ == '__main__':
    MyApp().run()