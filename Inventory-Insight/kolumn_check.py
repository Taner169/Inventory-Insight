import os
import pandas as pd
import csv
from mappLista import mapp_konfiguration

basvag = r'\\tingstad.tingstad.se\storage\jvsimport\supplier'

def kontrollera_kolumner(mapp, filtyp):
    full_vag = os.path.join(basvag, mapp, 'backup')
    if os.path.exists(full_vag):
        filer = [f for f in os.listdir(full_vag) if f.endswith(filtyp)]
        if filer:
            fil_väg = os.path.join(full_vag, filer[0])  # Använder endast den första filen
            try:
                if filtyp == 'csv':
                    df = pd.read_csv(fil_väg, on_bad_lines='skip', delimiter=';', quoting=csv.QUOTE_NONE)
                elif filtyp == 'txt':
                    df = pd.read_csv(fil_väg, delimiter='\t', encoding='ISO-8859-1', on_bad_lines='skip')
                print(f"Kolumner i {fil_väg}: {df.columns.tolist()}")
            except pd.errors.EmptyDataError:
                print(f"Fil är tom: {fil_väg}")
            except Exception as e:
                print(f"Ett fel inträffade vid läsning av filen {fil_väg}: {e}")

if __name__ == "__main__":
    for mapp, config in mapp_konfiguration.items():
        kontrollera_kolumner(mapp, config['filtyp'])
