import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import logging
from langchain.vectorstores import Chroma

from services.data_collectors.loaders import Loaders
from services.data_collectors.splitters import Splitters
from services.data_collectors.embeddings import Embeddings

class ChromaDB:
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.logger = logging.getLogger(__name__)
        self.embeddings = Embeddings().get_embeddings()
        self.vectordb = Chroma(
            embedding_function=self.embeddings,
            persist_directory="docs/datastore/chromadb",
        )

    def add_document(self, file_path, splitter_name="character"):
        try:
            loader = Loaders().file_loader(file_path)
            documents = loader.load()
            splitter = Splitters().split_document(splitter_name)
            docs = splitter.split_documents(documents)
            self.vectordb.add_documents(documents=docs, embedding=self.embeddings)
            self.logger.info("Added documents to database.")
        except Exception as e:
            self.logger.error(f"Error adding document: {e}")

    def similarity_search(self, query, top_n=10):
        """Performs similarity search on database."""
        try:
            results = self.vectordb.similarity_search(
                query, top_n=top_n
            )
            self.logger.info("Performed similarity search on database.")
            return results
        except Exception as e:
            self.logger.error(f"Error performing similarity search: {e}")


# TODO: Text mutable functionality

#    def add_mutable_document(self, page_content, document_id, page, collection_name="mutable_documents"):
#        document = Document(page_content=page_content, metadata={"page":page})
#        return self.db.from_documents(
#            documents =[document],
#            embedding=self.embeddings,
#            persist_directory=self.persistent_directory,
#            collection_name=collection_name,
#            ids=document_id
#            )
#
#    def update_mutable_document(self, page_content, document_id, page):
#        document = Document(page_content=page_content, metadata={"page":page})
#        return self.db.update_document(document, document_id)
#
