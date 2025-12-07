"""
Configuration centrale du projet
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration du système UEBA"""
    
    # Database
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", 5432))
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    
    # Elasticsearch
    ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST", "localhost")
    ELASTICSEARCH_PORT = int(os.getenv("ELASTICSEARCH_PORT", 9200))
    
    # Neo4j
    NEO4J_URI = os.getenv("NEO4J_URI")
    NEO4J_USER = os.getenv("NEO4J_USER")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
    
    # Kafka
    KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
    
    # Project
    PROJECT_NAME = os.getenv("PROJECT_NAME")
    VERSION = os.getenv("VERSION", "0.1.0")
    DEBUG = os.getenv("DEBUG", "False") == "True"
    
    @classmethod
    def get_postgres_url(cls):
        """Retourne l'URL de connexion PostgreSQL"""
        return f"postgresql://{cls.POSTGRES_USER}:{cls.POSTGRES_PASSWORD}@{cls.POSTGRES_HOST}:{cls.POSTGRES_PORT}/{cls.POSTGRES_DB}"
    
    @classmethod
    def get_elasticsearch_url(cls):
        """Retourne l'URL Elasticsearch"""
        return f"http://{cls.ELASTICSEARCH_HOST}:{cls.ELASTICSEARCH_PORT}"

config = Config()