from pathlib import Path
import json,sys
import pandas as pd
import skops.io as sio
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
def prohibido(*args,**kwargs):
    raise RuntimeError("Esta prueba prohíbe volver a entrenar")
Pipeline.fit=prohibido
TfidfVectorizer.fit=prohibido
TfidfVectorizer.fit_transform=prohibido
LogisticRegression.fit=prohibido
MultinomialNB.fit=prohibido
folder=Path(sys.argv[1])
tipos=sio.get_untrusted_types(file=folder/"baseline.skops")
if tipos:
    raise RuntimeError("Revisar tipos antes de autorizar la carga: "+str(tipos))
recuperado=sio.load(folder/"baseline.skops",trusted=[])
prueba=pd.read_csv(folder/"predicciones.csv",keep_default_na=False)
observadas=recuperado.predict(prueba.text_processed).tolist()
assert observadas==prueba.prediction.tolist(), "Predicciones distintas tras recarga"
resultado={"estado":"PASS","filas":len(prueba),"fit_prohibido":True,"tipos_no_confiables":tipos}
(folder/"recarga.json").write_text(json.dumps(resultado,indent=2))
print(json.dumps(resultado))
