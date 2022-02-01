from db import app
from routes import view_routes


view_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
