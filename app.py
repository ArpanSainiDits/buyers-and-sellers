from db import app 
from routes import view_routes
import sqlite3



con = sqlite3.connect("sb.db")
print("Database opened successfully")
con.close()




view_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
