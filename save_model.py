from create_model import create_model
from tensorflow import convert_to_tensor
import pandas as pd

df = pd.read_csv("out.csv")

traits_names = ["ambition1", "confidence1", "patience1", "kindness1", "creativity1", "resposibility1", "optimism1", "courage1", "modesty1", "perseverance1",
"ambition2", "confidence2", "patience2", "kindness2", "creativity2", "resposibility2", "optimism2", "courage2", "modesty2", "perseverance2"
]

match = df.pop("match")

ds = df[traits_names]
ds = convert_to_tensor(ds)

model = create_model()
model.fit(ds, match, epochs=25, batch_size=2)
model.save("saved_model/suggestion")