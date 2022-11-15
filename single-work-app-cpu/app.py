# app.py
import lightning as L

class YourComponent(L.LightningWork):
   def run(self):
      print('BENCHMARK 1 COMPLETE')

component = YourComponent()
app = L.LightningApp(component)