import os
import time
import requests
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#importar Base e BitcoinPReco do database
from database import Base, BitcoinPreco

#Carrega variáveis de ambiente do arquivo .env
load_dotenv()



