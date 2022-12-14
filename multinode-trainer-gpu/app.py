# app.py
import lightning as L
from lightning.app.components import MultiNode
from lightning.pytorch.demos.boring_classes import BoringModel


class LightningTrainerDistributed(L.LightningWork):
    @staticmethod
    def run():
        model = BoringModel()
        trainer = L.Trainer(max_epochs=10, strategy="ddp")
        trainer.fit(model)
        print('BENCHMARK DONE')

# 2 GPU nodes (keep the 4v100 nodes)...
# we want to make sure this cost is also going down...
# so we can benchmark it
component = MultiNode(
    LightningTrainerDistributed,
    num_nodes=2,
    cloud_compute=L.CloudCompute("gpu-multi-fast"), # 4 x v100
)
app = L.LightningApp(component)