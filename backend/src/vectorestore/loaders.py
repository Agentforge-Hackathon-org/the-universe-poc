from langchain.document_loaders import TextLoader, PyPDFLoader, UnstructuredHTMLLoader

class Loaders:
    def file_loader(self, file_path):
        if file_path.endswith(".txt"):
            return TextLoader(file_path=file_path)
        if file_path.endswith(".pdf"):
            return PyPDFLoader(file_path=file_path)
        if file_path.endswith(".html"):
            return UnstructuredHTMLLoader(file_path=file_path)
        else:
            return "File type not supported"