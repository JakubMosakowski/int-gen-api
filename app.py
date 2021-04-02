import random
from flask import Flask

app = Flask(__name__)

words = [
    "anchois",
    "bakłażan",
    "bazylia",
    "cytryny",
    "czosnek",
    "kapary",
    "kawa",
    "kiełbasa",
    "koper",
    "krewetki",
    "makaron",
    "mozarella",
    "mąka",
    "ocet",
    "olej",
    "oliwa",
    "oliwki",
    "oregano",
    "parmezan",
    "pepperoni",
    "pieczarki",
    "pietruszka",
    "pizza",
    "pomidor",
    "prosciutto",
    "ricotta",
    "rozmaryn",
    "rukola",
    "ser",
    "szpinak",
    "szpinak",
    "szynka",
    "wino",
    "woda"
]


# Annotation that allows the function to be hit at the specific URL. Indicates a GET HTTP method.
@app.route("/generate", methods=["GET"])
# Function that will run when the endpoint is hit.
def generate():
    generated_words = get_words()
    first = generated_words[0]
    second = generated_words[1]
    return f"{first} i {second}"


def get_words():
    rand_range = range(0, len(words) - 1)
    indexes = random.sample(rand_range, 2)

    first_word = words[indexes[0]]
    second_word = words[indexes[1]]
    return [
        first_word,
        second_word
    ]
