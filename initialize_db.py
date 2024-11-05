import sqlite3


conn = sqlite3.connect("chocolate_house.db") 
cursor = conn.cursor()


def create_tables():
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS SeasonalFlavors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
    """)
    
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS IngredientInventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ingredient_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            unit TEXT
        )
    """)
    
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CustomerSuggestions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            flavor_suggestion TEXT NOT NULL,
            allergy_concern TEXT
        )
    """)
    
    
    conn.commit()
    print("Database and tables created successfully!")


create_tables()
conn.close()
