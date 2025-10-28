import genanki
import random
from datetime import datetime

# Create a unique file name using the current date and time
current_time = datetime.now().strftime("%Y%m%d%H%M%S")
output_file = f"flashcards_{current_time}.apkg"

# Define the Anki model (use random IDs to avoid collisions)
model = genanki.Model(
    random.randrange(1 << 30, 1 << 31),
    'Simple Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card Template',
            'qfmt': '{{Question}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ],
)

# Create a deck
deck = genanki.Deck(
    random.randrange(1 << 30, 1 << 31),
    f"flashcards_{current_time}"
)

# Add flashcards to the deck
flashcards = [
    {
        "question": "What is the goal of physical activity for children aged 3-12 years?", 
        "answer": "The goal is to encourage movement through all types of physical activity."
    },
    {
        "question": "What is the focus for physical activity in children aged 0-3 years?", 
        "answer": "Encourage early movement to support development."
    },
    {
        "question": "What is emphasized in physical activity for children aged 3-5 years?", 
        "answer": "Expand on play and ensure activities are fun."
    },
    {
        "question": "What is the focus for children aged 5-8 years in physical activity?", 
        "answer": "Increase emphasis on fundamental movement skills."
    },
    {
        "question": "What physical activity goal is introduced for children aged 8-12 years?", 
        "answer": "Introduce more complex skills as children are developmentally ready."
    },
    {
        "question": "What is the primary focus of physical activity fundamentals for young children?", 
        "answer": "Focus on fun and limit competition to ensure enjoyment."
    },
    {
        "question": "Why is a developmentally appropriate framework important for teaching skills?", 
        "answer": "It ensures that skills are taught in a way that matches the child’s developmental stage."
    },
    {
        "question": "Why should specialization in sports occur later in childhood?", 
        "answer": "To equip kids with basic fundamental skills first and prepare them for lifelong activity involvement."
    },
    {
        "question": "What is the difference between sampling and single-sport focus in youth physical activity?", 
        "answer": "Sampling exposes children to various activities with limited competition, while single-sport focus is linked to early exit from the same sport."
    },
    {
        "question": "What are the benefits of sampling sports at a young age?", 
        "answer": "Exposure to diverse activities and reduced pressure from competition."
    },
    {
        "question": "Why is focusing on a single sport at a young age discouraged?", 
        "answer": "It is often associated with early burnout and dropping out of the sport."
    },
    {
        "question": "What does it mean to consider the 'whole person' in physical activity?", 
        "answer": "It involves understanding the contexts of physical activity and physical literacy, addressing emotional, physical, and social aspects."
    },
    {
        "question": "What is the long-term goal of teaching physical activity fundamentals to children?", 
        "answer": "To prepare them for a lifetime of involvement in physical activities."
    },
    {
        "question": "What is the primary goal of physical literacy in children?", 
        "answer": "To equip them with confidence and competence to engage in various physical activities."
    },
    {
        "question": "What is emphasized in physical activity for early childhood (ages 0-5)?", 
        "answer": "Encourage movement and expand play while ensuring activities are enjoyable."
    }
]
for card in flashcards:
    note = genanki.Note(
        model=model,
        fields=[card['question'], card['answer']]
    )
    deck.add_note(note)

# Save the deck as a .apkg file
genanki.Package(deck).write_to_file(output_file)
print(f"Deck exported to {output_file}")
print(len(flashcards))

# ---
# How to run this script:
# 1. Open a terminal and navigate to the folder containing this file (flashcards.py).
#    For example, if you are in the project folder, you can use:
#        cd /path/to/your/Flashcards
# 2. Make sure your virtual environment is activated (you should see (.venv) in your prompt).
# 3. Run the script with:
#        python flashcards.py
#
# This will generate a file named like 'flashcards_YYYYMMDDHHMMSS.apkg' in the same directory.
# You can then import this .apkg file into Anki.
