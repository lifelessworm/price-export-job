import pandas as pd
import os
from dotenv import load_dotenv

from paths import path

load_dotenv()

def consolidate_csvs():
    ars_folder = path('PATH_ARS_BASE', 'Ars')
    
    haipu_path = os.path.join(ars_folder, "PFOHAIPU", "PFOHAIPU.csv")
    path_5098 = os.path.join(ars_folder, "PFO5098", "PFO5098.csv")
    
    output_folder = os.path.join(ars_folder, "Output")
    final_path = os.path.join(ars_folder, "PFO5098p", "PFO5098p.csv")
    os.makedirs(os.path.dirname(final_path), exist_ok=True)

    try:
        
        print("Reading files...")
        df_haipu = pd.read_csv(haipu_path, sep=';', header=None, encoding='utf-8-sig')
        df_5098 = pd.read_csv(path_5098, sep=';', header=None, encoding='utf-8-sig')

        df_final = pd.concat([df_haipu, df_5098], axis=0, ignore_index=True)

        df_final.to_csv(final_path, index=False, header=False, sep=';', encoding='utf-8-sig')
        
        print(f"--- SUCCESS ---")
        print(f"Total Haipu rows: {len(df_haipu)}")
        print(f"Total 5098 rows: {len(df_5098)}")
        print(f"Consolidated file created with {len(df_final)} rows at: {final_path}")
        
        return final_path

    except Exception as e:
        print(f"Error joining the files: {e}")
        return None

if __name__ == "__main__":
    consolidate_csvs()
