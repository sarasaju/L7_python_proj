from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("chocolate_house.db")
    conn.row_factory = sqlite3.Row  
    return conn


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/flavors')
def view_flavors():
    conn = get_db_connection()
    flavors = conn.execute("SELECT * FROM SeasonalFlavors").fetchall()
    conn.close()
    return render_template("flavors.html", flavors=flavors)



@app.route('/add_flavor', methods=["GET", "POST"])
def add_flavor():
    if request.method == "POST":
        flavor = request.form['flavor'] 
        description = request.form['description']  
        conn = get_db_connection()
        conn.execute("INSERT INTO SeasonalFlavors (name, description) VALUES (?, ?)", (flavor, description))
        conn.commit()
        conn.close()
        return redirect(url_for('view_flavors'))
    return render_template("add_flavor.html")


@app.route('/inventory')
def view_inventory():
    conn = get_db_connection()
    ingredients = conn.execute("SELECT * FROM IngredientInventory").fetchall()
    conn.close()
    return render_template("inventory.html", ingredients=ingredients)

@app.route('/add_ingredient', methods=["GET", "POST"])
def add_ingredient():
    if request.method == "POST":
        ingredient_name = request.form['ingredient_name']  
        quantity = request.form['quantity']  
        unit = request.form['unit']  
        
        conn = get_db_connection()
        conn.execute("INSERT INTO IngredientInventory (ingredient_name, quantity, unit) VALUES (?, ?, ?)", 
                     (ingredient_name, quantity, unit))
        conn.commit()
        conn.close()
        
        return redirect(url_for('view_inventory'))
    return render_template("add_ingredient.html")


@app.route('/suggestions')
def view_suggestions():
    conn = get_db_connection()
    suggestions = conn.execute("SELECT * FROM CustomerSuggestions").fetchall()
    conn.close()
    return render_template("suggestions.html", suggestions=suggestions)

@app.route('/add_suggestion', methods=["GET", "POST"])
def add_suggestion():
    if request.method == "POST":
        customer_name = request.form['customer_name']  
        flavor_suggestion = request.form['flavor_suggestion']  
        allergy_concern = request.form['allergy_concern']  
        
        conn = get_db_connection()
        conn.execute("INSERT INTO CustomerSuggestions (customer_name, flavor_suggestion, allergy_concern) VALUES (?, ?, ?)",
                     (customer_name, flavor_suggestion, allergy_concern))
        conn.commit()
        conn.close()
        
        return redirect(url_for('view_suggestions'))
    return render_template("add_suggestion.html")



if __name__ == "__main__":
    app.run(debug=True)
