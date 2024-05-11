from pymongo import MongoClient, UpdateOne, InsertOne
import pandas as pd
from config import MongoDBConfig

WALLETS_COL = 'depositWallets'


class MongoDB:
    def __init__(self, connection_url=None, chain_id: str = ""):
        if not connection_url:
            connection_url = MongoDBConfig.CONNECTION_URL

        self.connection_url = connection_url.split('@')[-1]
        self.connection = MongoClient(connection_url)
        self._db = self.connection[MongoDBConfig.DATABASE]
        self.lp_tokens_col = self._db['lpTokens']
        self._deposit_wallets_col = self._db['depositWallets']
        # self.wallets_col = self._db[WALLETS_COL]
        self._groups_col = self._db['groups']
        self._tweets = self._db['tweets']
        self._transactions_col = self._db[f'{chain_id}_transactions']
        self._token_transfers_col = self._db['token_transfers']


    #######################
    #       Generals      #
    #######################
    def count_documents(self, col_name):
        return self._db[col_name].estimated_document_count()

    def get_documents(self, col_name: str, skip: int, limit: int):
        return self._db[col_name].find({}).skip(skip).limit(limit)

    def get_documents_by_ids(self, col_name: str, ids: list):
        return self._db[col_name].find({'_id': {'$in': ids}})

    #######################
    #   get tweets info   #
    #######################

    def get_tweet(self):
        tweets_lst = []
        cursor = self._tweets.find()
        for da in cursor:
            da_dct ={}
            da_dct['authorName'] = da['authorName']
            da_dct['timestamp'] = da['timestamp']
            if 'quotedTweet' in da:
                additional_text = da['quotedTweet']['text']
                da_dct['content'] = 'Author: '+da['authorName']+'; Content: ' +da['text'] + '\n\n' + additional_text
            else:
                da_dct['content'] = 'Author: '+da['authorName']+'; Content: ' +da['text']
            tweets_lst.append(da_dct)
            df_twitter = pd.DataFrame(tweets_lst)
        return df_twitter

    #######################
    #   updates   #
    #######################


    def update_data(self, name, data):
        bulk_updates = [
            UpdateOne({'_id': datum['_id']}, {'$set': datum}, upsert=True
            )
            for datum in data
       ]
        self._db[f"{name}"].bulk_write(bulk_updates)

