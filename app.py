from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the home page with links to Fortune and Weather."""
    return render_template('index.html')

@app.route('/fortune')

@app.route('/fortune_results')
def fortune_results():
    """Displays the user's fortune."""
    users_favorite_animal = request.args.get('animal')
    # ... etc

    if users_favorite_animal == 'Whale':
        print(f"You'll have a magical day!")
        # fortune is "You'll have a magical day!"
    elif users_favorite_animal == 'Bear':
        print(f"You'll have good luck for 10 years!")
        # fortune is ...
    elif users_favorite_animal == "Unicorn":
        print(f"You will find a puppy at your doorstep tomorrow.")
        # fortune is ...
    else:
        return render_template('fortune.html')
        # no other fortune applies, return default fortune