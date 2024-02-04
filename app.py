from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profil')
def profil():
    return render_template('profil.html')

@app.route('/projets')
def projets():
    return render_template('projets.html')

@app.route('/projet_pentesting')
def projet_pentesting():
    return render_template('projet_pentesting.html')

@app.route('/passions')
def passions():
    return render_template('passions.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    response = get_bot_response(user_input)
    return render_template('index.html', user_input=user_input, response=response)

def get_bot_response(user_input):
    # Implémentez la logique du chatbot ici
    # Par exemple, utilisez des conditions pour répondre à différentes questions
    
    if "objectif" in user_input.lower() or "avenir" in user_input.lower() or "d'avenir" in user_input.lower() or "projet d'avenir" in user_input.lower():
        return "Je souhaiterais réaliser un parcours bac +5 pour me spécialiser dans le développement et la cybersécurité"

    elif "dernier projet" in user_input.lower():
        return "Mon dernier projet est un projet de Pentesting sur une machine virtuelle. Je vous laisse l'accès à l'aide de ce lien : http://127.0.0.1:5000/projet_pentesting "

    elif "centres d'interets" in user_input.lower() or "interets" in user_input.lower():
        return "Mes centres d'intérêt sont le ski, le surf, le football, le développement web et les jeux vidéos."

    elif " age" in user_input.lower():
        return "J'ai 19 ans."

    elif "prenom" in user_input.lower():
        return "Je m'appelle Damien."

    elif "nom de famille" in user_input.lower():
        return "Mon nom de famille est Villevet."

    elif "parcours" in user_input.lower():
        return "Je suis actuellement en BUT Réseaux et Télécommunications."

    elif "passions" in user_input.lower():
        return "Mes passions incluent le ski, le surf, le football, le développement web et les jeux vidéos."

    elif "projet" in user_input.lower():
        return "Je travaille sur des projets de pentesting, d'IoT et de chatbot."

    # Ajoutez d'autres conditions pour d'autres questions

    return "Je ne comprends pas la question."





if __name__ == '__main__':
    app.run(debug=True)
