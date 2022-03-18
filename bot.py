import logging
from telegram.ext import Updater

# Configurar Logging

logging.basicConfig(
    level = logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,"
)

logger = logging.getLogger()

# Solicitar Token

TOKEN = "5231783723:AAFviOKHaUZ9fpDEGJWkwNIvsCqCVb9ScAI"
