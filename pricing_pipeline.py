import sys
import os

try:
    from csv_export_4091 import parts_online as parts_4091
    from csv_export_4091p import parts_online as parts_4091p
    from csv_export_haipu import parts_online as parts_haipu
    from csv_export_5098 import parts_online as parts_5098
    from csv_merger import consolidate_csvs
    from file_compressor import zip_file_4091, zip_file_5098, zip_file_4091p, zip_file_5098p
    from email_sender import send_files_by_email

except ImportError as e:
    print(f"Error importing modules: {e}")
    sys.exit(1)

if getattr(sys, 'frozen', False):
    root_folder = os.path.dirname(sys.executable)

else:
    root_folder = os.path.dirname(os.path.abspath(__file__))

output_folder = os.path.join(root_folder, "Output")

def run_routine():
    print("=== STARTING MASTER SYSTEM ===")

    print("\n[STEP 1] Extracting data from Oracle...")
    parts_haipu()
    parts_4091()
    parts_4091p()
    parts_5098()

    print("\n[STEP 2] Starting Consolidator (Concatenation)...")
    unified_file = consolidate_csvs()
    
    if unified_file:
        print("\n[STEP 3] Compressing file to Output...")
        zip_file_4091()
        zip_file_5098()
        zip_file_4091p()
        zip_file_5098p()
    else:
        print("\n[ERROR] The consolidator did not generate the unified file.")

    print("\n[STEP 4] Sending files by e-mail...")
    send_files_by_email()

    print("\n=== PROCESS FINISHED SUCCESSFULLY ===")

if __name__ == "__main__":
    run_routine()
