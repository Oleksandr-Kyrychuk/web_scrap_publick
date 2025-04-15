import requests
from bs4 import BeautifulSoup
import csv
import logging
import re
import time
import unicodedata
import random
import os
import gzip
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Налаштування логування
logging.basicConfig(filename="workua_scraper.log", level=logging.INFO)

# Конфігурація дебагінгу
DEBUG_MODE = False  # Увімкнути для збереження всіх HTML-файлів


def create_vacancy_pattern(search_vacancy):
    """
    Створює регулярний вираз для пошуку вакансій за введеним запитом.

    Args:
        search_vacancy (str): Назва вакансії для пошуку (наприклад, "Водій").

    Returns:
        str: Регулярний вираз для відповідності назви вакансії.
    """
