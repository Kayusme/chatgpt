import PyPDF2


class PdfReader:
    def __init__(self):
        self.texts = []

    def upload(self, pdf_path):
        pdf_file = open(pdf_path, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        num_pages = pdf_reader.numPages

        for page in range(num_pages):
            page_obj = pdf_reader.getPage(page)
            self.texts.append(page_obj.extractText())

        pdf_file.close()

    def get_text(self):
        return self.texts
