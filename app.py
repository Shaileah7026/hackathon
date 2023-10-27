from flask import Flask, render_template, request, jsonify
from chat import get_answer

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def response():
    if request.method == "POST":
        user_Query = request.form.get('userQuery')  # Retrieve data from the form
        answer = get_answer(user_Query)
        return jsonify({"answer": answer})  # Return the answer as JSON
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
