import zipfile
import os
from dotenv import load_dotenv

from paths import path

load_dotenv()

def zip_file_5098():
    output_folder = path('PATH_ZIP_OUTPUT', os.path.join('Output'))
    base_folder = path('PATH_ARS_BASE', 'Ars')
    subfolder = "PFO5098"
    csv_name = "PFO5098.csv"
    zip_name = "PFO5098.zip"
    
    csv_path = os.path.join(base_folder, subfolder, csv_name)
    zip_path = os.path.join(output_folder, zip_name)


    if os.path.exists(csv_path):
        try:
            print(f"Locating file: {csv_name}...")
            
            os.makedirs(os.path.dirname(zip_path), exist_ok=True)
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(csv_path, arcname=csv_name)
            
            print(f"Success! File compressed to: {zip_path}")
            
        except Exception as e:
            print(f"Error compressing: {e}")
    else:
        print(f"Error: File {csv_path} was not found.")

if __name__ == "__main__":
    zip_file_5098()

def zip_file_4091():
    output_folder = path('PATH_ZIP_OUTPUT', os.path.join('Output'))
    base_folder = path('PATH_ARS_BASE', 'Ars')
    subfolder = "PFO4091"
    csv_name = "PFO4091.csv"
    zip_name = "PFO4091.zip"
    
    csv_path = os.path.join(base_folder, subfolder, csv_name)
    zip_path = os.path.join(output_folder, zip_name)

    if os.path.exists(csv_path):
        try:
            print(f"Locating file: {csv_name}...")
            
            os.makedirs(os.path.dirname(zip_path), exist_ok=True)
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(csv_path, arcname=csv_name)
            
            print(f"Success! File compressed to: {zip_path}")
            
        except Exception as e:
            print(f"Error compressing: {e}")
    else:
        print(f"Error: File {csv_path} was not found.")

if __name__ == "__main__":
    zip_file_4091()

def zip_file_4091p():
    output_folder = path('PATH_ZIP_OUTPUT', os.path.join('Output'))
    base_folder = path('PATH_ARS_BASE', 'Ars')
    subfolder = "PFO4091p"
    csv_name = "PFO4091p.csv"
    zip_name = "PFO4091p.zip"
    
    csv_path = os.path.join(base_folder, subfolder, csv_name)
    zip_path = os.path.join(output_folder, zip_name)

    if os.path.exists(csv_path):
        try:
            print(f"Locating file: {csv_name}...")
            
            os.makedirs(os.path.dirname(zip_path), exist_ok=True)
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(csv_path, arcname=csv_name)
            
            print(f"Success! File compressed to: {zip_path}")
            
        except Exception as e:
            print(f"Error compressing: {e}")
    else:
        print(f"Error: File {csv_path} was not found.")

if __name__ == "__main__":
    zip_file_4091p()

def zip_file_5098p():
    output_folder = path('PATH_ZIP_OUTPUT', os.path.join('Output'))
    base_folder = path('PATH_ARS_BASE', 'Ars')
    subfolder = "PFO5098p"
    csv_name = "PFO5098p.csv"
    zip_name = "PFO5098p.zip"
    
    csv_path = os.path.join(base_folder, subfolder, csv_name)
    zip_path = os.path.join(output_folder, zip_name)

    if os.path.exists(csv_path):
        try:
            print(f"Locating file: {csv_name}...")
            
            os.makedirs(os.path.dirname(zip_path), exist_ok=True)
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(csv_path, arcname=csv_name)
            
            print(f"Success! File compressed to: {zip_path}")
            
        except Exception as e:
            print(f"Error compressing: {e}")
    else:
        print(f"Error: File {csv_path} was not found.")

if __name__ == "__main__":
    zip_file_5098p()
