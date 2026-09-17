# app.py – Gästbok

from flask import Flask, request, render_template, redirect
from datetime import datetime
import json
import os

app = Flask(__name__)
DATA_FILE = 'data.json'


def load_posts():
    #Läser in alla inlägg från JSON-filen och returnerar dem som en listaav dictionaries. Om filen inte finns än returneras en tom lista.
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, encoding='utf-8') as f:
        return json.load(f)


def save_posts(posts):
    #Sparar hela listan med inlägg som JSON i DATA_FILE.
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(posts, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')