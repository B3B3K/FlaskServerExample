from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test_index.html')

@app.route('/execute', methods=['POST'])
def execute_function():
    # Function logic goes here
    # This code will execute when the button is clicked
    print("ok!")
    return 'Function executed successfully!'



if __name__ == '__main__':
    app.run()
