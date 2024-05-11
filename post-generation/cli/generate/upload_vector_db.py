import click
import pandas as pd
import numpy as np
from llama_index.core.schema import TextNode
from databases.mongodb import MongoDB
from databases.postgresql import PostgresDB
from models.embedding_models import EmbeddingModel
from utils.logger_utils import get_logger
@click.command(context_settings=dict(help_option_names=['-h', '--help']))

def upload_vector_db():
    logg = get_logger("Embedding storage")
    logg.info("Start to connect model and database ...")
    embed_model = EmbeddingModel()
    mongo_db = MongoDB()
    posgre_db = PostgresDB()
    logg.info("Start to get tweet data ...")

    df_tweet = mongo_db.get_tweet()
    logg.info("Sucessful get tweet")
    nodes = []
    logg.info("Start to get embed tweets ...")

    for index, row in df_tweet.iterrows():
        node = TextNode(text=row['content'], id_=f"{row['authorName']}_{row['timestamp']}")
        nodes.append(node)


    logg.info("Sucessful embed tweets")

    for node in nodes:
        node_embedding = embed_model._embed_model.get_text_embedding(
            node.get_content(metadata_mode="all")
        )
        node.embedding = node_embedding

    logg.info("Sucessful upload vectordb")

    posgre_db.vetor_store.add(nodes)