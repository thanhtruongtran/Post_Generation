from sqlalchemy.orm import sessionmaker
from config import PostgresRAGDBConfig, EmbeddingModelConfig
from utils.logger_utils import get_logger
from utils.postgres_utils import extract_db_details
from llama_index.vector_stores.postgres import PGVectorStore

logger = get_logger('PostgreSQL thread safe')
Session = sessionmaker()


class PostgresDB:
    def __init__(self, connection_url: str = None):
        # Set up the database connection and create the table
        if not connection_url:
            connection_url = PostgresRAGDBConfig.CONNECTION_URL
        self.db_name, self.host, self.password, self.port, self.user = extract_db_details(connection_url)
        self.vetor_store = PGVectorStore.from_params(
                                database=self.db_name,
                                host=self.host,
                                password=self.password,
                                port=self.port,
                                user=self.user,
                                table_name=PostgresRAGDBConfig.RAG_TABLE,
                                embed_dim=int(EmbeddingModelConfig.EMBEDDING_DIMENSION))



