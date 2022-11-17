# app.py
import lightning as L


class YourComponent(L.LightningWork):
   def run(self):
      print('BENCHMARK DONE')

# run on a cloud machine ("cpu", "gpu", ...)
compute = L.CloudCompute("gpu")
component = YourComponent(cloud_compute=compute)
app = L.LightningApp(component)