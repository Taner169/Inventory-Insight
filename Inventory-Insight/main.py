import os
import pandas as pd
import csv
from mappLista import mapp_konfiguration

basvag = r'\\tingstad.tingstad.se\storage\jvsimport\supplier'
csv_mapp = 'csv_data'

if not os.path.exists(csv_mapp):
    os.makedirs(csv_mapp)

def rensa_citationstecken(kolumner):
    if kolumner is not None:
        rensade_kolumner = [k.replace('"', '').strip() for k in kolumner]
        if rensade_kolumner:
            rensade_kolumner[0] = rensade_kolumner[0].lstrip('\ufeff')  # Ta bort BOM
        return rensade_kolumner
    return None

def spara_till_csv(df, mappnamn, filnamn):
    csv_fil_väg = os.path.join(csv_mapp, f"{mappnamn}_{filnamn}.csv")
    df.to_csv(csv_fil_väg, index=False)
    print(f"Sparar data till {csv_fil_väg}")

def las_och_spara_filer(mapp, filtyp, kolumner=None, has_header=True, delimiter=';'):
    full_vag = os.path.join(basvag, mapp, 'backup')
    filer = [os.path.join(full_vag, f) for f in os.listdir(full_vag) if f.endswith(filtyp)]
    for fil_väg in filer:
        try:
            try:
                df = pd.read_csv(fil_väg, on_bad_lines='skip', delimiter=delimiter, quoting=csv.QUOTE_NONE, encoding='utf-8-sig')
            except UnicodeDecodeError:
                df = pd.read_csv(fil_väg, on_bad_lines='skip', delimiter=delimiter, quoting=csv.QUOTE_NONE, encoding='ISO-8859-1')
            
            df.columns = [col.lstrip('\ufeff') for col in df.columns]  # Ta bort BOM om det finns
            
            if has_header and kolumner is not None:
                df.columns = rensa_citationstecken(df.columns.tolist())
                if not set(kolumner).issubset(df.columns):
                    raise KeyError(f"En eller flera av de specificerade kolumnerna {kolumner} hittades inte i CSV-filen med kolumner {df.columns.tolist()}.")
                df = df[kolumner]
            elif not has_header:
                df = pd.read_csv(fil_väg, header=None, names=kolumner, on_bad_lines='skip', delimiter=delimiter, quoting=csv.QUOTE_NONE, encoding='ISO-8859-1')
            
            filnamn = os.path.basename(fil_väg).split('.')[0]
            spara_till_csv(df, mapp, filnamn)
        except Exception as e:
            print(f"Ett fel inträffade vid läsning av filen {fil_väg}: {e}")

for mapp, config in mapp_konfiguration.items():
    kolumner = None
    if 'kolumner' in config and config['kolumner'] is not None:
        kolumner = rensa_citationstecken(config['kolumner'])
    delimiter = config.get('delimiter', ';')
    las_och_spara_filer(mapp, config['filtyp'], kolumner, config.get('has_header', True), delimiter)

