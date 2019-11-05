from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the home page with links to Fortune and Weather."""
    return render_template('index.html')

@app.route('/fortune')
def fortune_form():
    """Displays fortune form."""
    return render_template('fortune_form.html')

@app.route('/fortune_results')
def fortune_results():
    """Displays the user's fortune."""
    users_favorite_animal = request.args.get('animal')

    if users_favorite_animal == 'Whale':
        fortune= "You'll have a magical day!"

    elif users_favorite_animal == 'Bear':
        fortune= "You'll have good luck for 10 years!"

    elif users_favorite_animal == "Unicorn":
        fortune = "You will find a puppy at your doorstep tomorrow."
       
    else:
        fortune= "Good luck."

    return render_template('fortune_results.html', fortune=fortune)
       
