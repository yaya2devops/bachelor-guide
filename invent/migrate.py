import shutil
import os


# The purpose of this script to get pdf author works and serve it under create.ya-ya.tech/service.pdf
# List of PDF files
pdf_files = [
    "./docs/pfe/snapshot.pdf",
    "./docs/hello/Hello Yaya/Hello_Yaya.pdf",
    "./docs/lifeline/him/vite-svp/accelerate.pdf",
    "./docs/lifeline/him/vite-svp/accelerate-x.pdf",
    "./docs/lifeline/content.pdf",
    "./docs/images/latex/2-prompt-5-pages.pdf",
    "./docs/images/InternsAssets/attes.pdf",
    "./docs/images/InternsAssets/Convention-Stage-ete.pdf",
    "./docs/images/InternsAssets/gen-latex-prompt.pdf",
    "./docs/images/InternsAssets/Journal-de-stage.pdf",
    "./docs/pfa/pfa.pdf",
    "./invent/assets/manifest.pdf",
    "./invent/assets/flash.pdf"
]

destination_dir = "./take-em-bruh"

os.makedirs(destination_dir, exist_ok=True)

# Copy each PDF file to the destination directory
for file in pdf_files:
    if os.path.exists(file):
        shutil.copy(file, destination_dir)
        print(f"Copied {file} to {destination_dir}")
    else:
        print(f"File not found: {file}")
