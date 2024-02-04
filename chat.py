import openai

# Remplacez 'YOUR_API_KEY' par votre clé API
openai.api_key = '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'

# Exemple de question
question = "Quel âge as-tu ?"

# Appel à l'API GPT-3
response = openai.Completion.create(
    engine="text-davinci-003",  # Vous pouvez choisir un autre moteur en fonction de vos besoins
    prompt=question,
    max_tokens=150  # Limitez le nombre de tokens générés si nécessaire
)

# Affichage de la réponse
print(response.choices[0].text.strip())
