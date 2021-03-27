from os import getenv
from pymongo import MongoClient
import urllib.parse
from bson.objectid import ObjectId

dbUri = 'mongodb://%s:%s' % (getenv('DB_URL'), getenv('DB_PORT'))
if getenv('DB_USERNAME') != None:
    dbUri = 'mongodb://%s:%s@%s:%s' % (urllib.parse.quote_plus(getenv('DB_USERNAME')),
                                       urllib.parse.quote_plus(getenv('DB_PASSWORD')), getenv('DB_URL'), getenv('DB_PORT'))

client = MongoClient(dbUri)
db = client[getenv('DB_NAME')]


def addDebt(address, tx, amount):
    db.debt.insert_one({
        'address': address,
        'tx': tx,
        'amount': amount
    })


def getAllDebt(address):
    return db.debt.find({'address': address})


def deleteOneDebt(tx):
    db.debt.delete_one({'tx': tx})
