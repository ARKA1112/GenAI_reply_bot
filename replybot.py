import tweepy
from airtable import Airtable
from datetime import datetime, timedelta
from langchain.chat_models import ChatVertexAI
from langchain.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
import schedule
import time
import os


# Helpful when testing locally

from dotenv import load_dotenv
load_dotenv()


# Twitterbot class to help us organize our

class TwitterBot:
    def __inti__(self):
        self.