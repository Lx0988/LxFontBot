import os

class Config(object):

      BOT_TOKEN = os.environ.get("BOT_TOKEN", "5444048309:AAEK4hg-6xAEjLhj2N2exVpTwhGtg9G4kRo")
      API_ID = int(os.environ.get("API_ID", 16029596))
      API_HASH = os.environ.get("API_HASH", "8c6b3ce7f23e51dfebbdbe98a0ee674d")
      OWNER_ID = int(os.environ.get("OWNER_ID", "1903280447"))

