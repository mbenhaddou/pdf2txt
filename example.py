from pdf2txt.core import Document
import pytesseract
import os, re#, cv2
from pdf2txt.utils import TemporaryDirectory, get_page_layout, convert_pdf_to_image
import pdf2image
import regex as reg
from pdf2txt.doc_analyzer.image_analyzer import PageAnalyzer
#region_extractor=RegionExtractor()
from pdf2txt import PdfReader
pdf0 = "/Users/mohamedmentis/Dropbox/My Mac (MacBook-Pro.local)/Documents/Mentis/Development/Python/candriam_entities_api/pdfs/Aviva Investors Global Convertibles Absolute Return Fund Class I - Factsheet.pdf"
pdf1 = "pdfs/BNP Euro Valmeurs Durables.pdf"
pdf2 = "pdfs/Carmignac Grande Europe Factsheet_LU0099161993_LU_EN.pdf"
pdf3 = "pdfs/Fidelity Sustainable Eurozone Equity Factsheet LU0238202773.pdf"
pdf4 = "/Users/mohamedmentis/Dropbox/My Mac (MacBook-Pro.local)/Documents/Mentis/Development/Python/candriam_entities_api/pdfs/JPM Global Convertibles (EUR) I (acc) - EUR.pdf"
pdf5 = "pdfs/LFDE Major growth Europe - Factsheet - FR-FR0010321828.pdf"
pdf6 = "pdfs/Nordea European Equity Starts Facsheet.pdf"
pdf7 = "pdfs/OFI Invest Ethical European Equity.pdf"
pdf8 = "/Users/mohamedmentis/Dropbox/My Mac (MacBook-Pro.local)/Documents/Mentis/Development/Python/candriam_entities_api/pdfs/LO Funds - Convertible Bonds.pdf"
pdf9 = "/Users/mohamedmentis/Dropbox/My Mac (MacBook-Pro.local)/Documents/Mentis/Development/Python/candriam_entities_api/pdfs/CamGestion_Convertibles_Europe_Part_I.pdf"
pdf10="/Users/mohamedmentis/Dropbox/My Mac (MacBook-Pro.local)/Documents/Mentis/Development/Python/candriam_entities_api/pdfs/Ecofi Convertibles Euro_FR0010191908.pdf"
pdf11="/Users/mohamedmentis/Dropbox/My Mac (MacBook-Pro.local)/Documents/Mentis/Clients/CANDIAM/POC_Structuration/Factsheets Convertibles/dnca-invest-convertibles_lu0401808935.pdf"
pdf12="/Users/mohamedmentis/Dropbox/My Mac (MacBook-Pro.local)/Documents/Mentis/Clients/CANDIAM/POC_Structuration/Fact sheets/CGF_HBFU_I-fact-202006-proffrfr.pdf"
pdf13 = "/Users/mohamedmentis/Dropbox/My Mac (MacBook-Pro.local)/Documents/Mentis/Development/Python/candriam_entities_api/pdfs/dnca-invest-convertibles_lu0401808935.pdf"
pdf21= "/Users/mohamedmentis/Dropbox/My Mac (MacBook-Pro.local)/Documents/Mentis/Clients/CANDIAM/POC_Structuration/templateequityfacshseets/Aviva Investors Valeurs Europe Class I - Reporting mensuel_trimestriel.pdf"


from poppdf import PdfDocument


def read(path):


    with TemporaryDirectory() as tempdir:
        pages = convert_from_path(path, dpi=150)
        for i, page in enumerate(pages):
            temp_path = os.path.join(tempdir, f"page-{i}.png")
            page.save(temp_path)

            orig_im = cv2.imread(temp_path)

            pdf = pytesseract.image_to_pdf_or_hocr(orig_im, extension='pdf')
            pdf_path = temp_path.replace('.png', '.pdf')
            with open(pdf_path, 'wb') as out:
                out.write(pdf)
            layout, dims = get_page_layout(pdf_path)

#            pages.append(page)
            os.remove(temp_path)


def run_from_folder( folder_path):
    import glob
    for filename in glob.glob(os.path.join(folder_path, '*.pdf')):
        print(filename)
        pdf_doc=Document.open(filename)
#        pdf_doc.pages[1].detect_semantic_structure()
        for page in pdf_doc.pages[0:4]:
            page.detect_semantic_structure(debug=True)
        print(pdf_doc.Text)

def run_file(filename):

    pdf_doc = Document.open(filename)

    for page in pdf_doc.pages:
        page.detect_semantic_structure()
#        print(page.Text)
        print("=============================")

    print(pdf_doc.Title)
    print(pdf_doc.Text)

    for paragraph in pdf_doc.paragraphs:
        print(paragraph)

pdf10="/Users/mohamedmentis/Dropbox/My Mac (MacBook-Pro.local)/Documents/Mentis/Development/Python/candriam_entities_api/pdfs/Aviva Investors Global Convertibles Absolute Return Fund Class I - Factsheet.pdf"
pdf3 = "/Users/mohamedmentis/Dropbox/Mac (2)/Documents/Mentis/Development/Projects/RL_Article/1906.03926.pdf"
pdf22="/Users/mohamedmentis/Dropbox/My Mac (MacBook-Pro.local)/Documents/Mentis/Development/Python/candriam_entities_api/pdfs/JPM Global Convertibles (EUR) I (acc) - EUR.pdf"

def load_pdf(file_path):

    pdf = PdfReader(file_path)

    return pdf.extract_text()

print(load_pdf(pdf3))
#run_from_folder("pdf3")



