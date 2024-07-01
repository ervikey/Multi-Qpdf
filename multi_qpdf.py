import os
import subprocess
import glob

# Define the output directory
output_dir = "output"

# Check if the output directory exists, if not, create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print("Output directory created.")
else:
    print("Output directory exists.")

# Prompt for the password once
password = input("Enter password for the PDF files: ")

# Loop through all PDF files in the current directory
pdf_files = glob.glob("*.pdf")

if not pdf_files:
    print("No PDF files found.")
else:
    for eachfile in pdf_files:
        print(f"Processing {eachfile}")
        output_file = os.path.join(output_dir, eachfile)
        try:
            subprocess.run(
                ["qpdf", f"--password={password}", "--decrypt", eachfile, output_file],
                check=True
            )
        except subprocess.CalledProcessError as e:
            print(f"Failed to decrypt {eachfile}: {e}")

print("Processing complete.")
