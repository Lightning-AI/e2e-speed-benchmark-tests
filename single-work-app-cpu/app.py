# app.py
import lightning as L

class YourComponent(L.LightningWork):
   def run(self):
      print('BENCHMARK DONE')

component = YourComponent()
app = L.LightningApp(component)