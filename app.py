from db import app
import routes.books
import routes.members
import routes.borrow

if __name__ == "__main__":
    app.run(debug=True, port=5000)
