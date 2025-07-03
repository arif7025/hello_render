from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def hello():
    return "Hello, World from Render!"

# Start the app if the script is run directly
if __name__ == '__main__':
    app.run(debug=True)
