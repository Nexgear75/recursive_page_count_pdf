import os
import PyPDF2
import subprocess

def count_pages(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfFileReader(file)
            return pdf_reader.numPages
    except Exception as e:
        print(f"Erreur lors du traitement du fichier '{pdf_path}': {e}")
        return 0

def count_pages_in_directory(directory):
    total_pages = 0
    problematic_files = []

    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.pdf'):
                file_path = os.path.join(foldername, filename)
                num_pages = count_pages(file_path)
                if num_pages > 0:
                    total_pages += num_pages
                else:
                    problematic_files.append(file_path)

    return total_pages, problematic_files

if __name__ == "__main__":
    current_directory = os.getcwd()

    total_pages, problematic_files = count_pages_in_directory(current_directory)

    print(f"Nombre total de pages dans les fichiers PDF dans le dossier courant : {total_pages}")

    if problematic_files:
        print("\nFichiers ayant rencontré un problème :")
        for file_path in problematic_files:
            print(file_path)

    input("\nAppuyez sur Entrée pour quitter...")
