import json
from typing import List
from src.models.credit_card import CreditCard

DATA_FILE = 'data/credit_cards.json'

def save_cards(cards: List[CreditCard]) -> None:
    with open(DATA_FILE, 'w') as f:
        json.dump([card.__dict__ for card in cards], f)

def load_cards() -> List[CreditCard]:
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        return [CreditCard(**card_data) for card_data in data]
    except FileNotFoundError:
        return []