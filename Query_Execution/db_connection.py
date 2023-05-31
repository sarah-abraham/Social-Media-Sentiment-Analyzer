import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()
def connection():
    uri = os.getenv('DB_URI')
    print(uri)
    username = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    graph = GraphDatabase.driver(uri, auth=(username, password))
    return graph