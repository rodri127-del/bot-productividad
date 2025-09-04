import tweepy
import random
import os

# Configuración de la API
client = tweepy.Client(
    bearer_token=os.getenv("BEARER_TOKEN"),
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_SECRET")
)

# Hashtags de productividad
hashtags = [
    "#Productividad", "#Trabajo", "#Focus", "#Hábitos", "#Organización",
    "#Notion", "#Canva", "#Grammarly", "#Tecnología", "#Aprendizaje",
    "#IA", "#Herramientas", "#TrabajoDesdeCasa"
]

# Lee frases y herramientas
with open('frases_productividad.txt', 'r', encoding='utf-8') as f:
    frases = [line.strip() for line in f.readlines() if line.strip()]

try:
    with open('herramientas.txt', 'r', encoding='utf-8') as f:
        herramientas = [line.strip() for line in f.readlines() if line.strip()]
except FileNotFoundError:
    herramientas = []

# Decide: 80% frase, 20% herramienta
if herramientas and random.random() < 0.2:
    tweet = random.choice(herramientas) + " " + " ".join(random.sample(hashtags, 2))
else:
    frase = random.choice(frases)
    tweet = frase + " " + " ".join(random.sample(hashtags, 3))

# Publica
client.create_tweet(text=tweet)
print(f"✅ Tweet publicado: {tweet}")
