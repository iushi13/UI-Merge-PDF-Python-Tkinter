from PyPDF2 import PdfReader, PdfMerger


def merge_pdfs(filepaths, savepath):
    # Create PdfMerger object
    merger = PdfMerger()

    # Merge selected files
    for filepath in filepaths:
        with open(filepath, 'rb') as file:
            merger.append(PdfReader(file))

    # Save merged file
    with open(savepath, 'wb') as output_file:
        merger.write(output_file)
