from flask import Flask, render_template, request, jsonify
from chat import get_answer

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def response():
    if request.method == "POST":
        user_query = request.form.get('userQuery')
        answer = get_answer(user_query)
        
        try:
            return jsonify({"answer": answer})  # Return the answer as JSON
        except TypeError:
            # If answer is not serializable, extract necessary information
            answer_data = str(answer)  # Or extract required data in a format jsonify can handle
            return jsonify({"answer": answer_data})
    return render_template("index.html")

@app.route('/db', methods=['GET', 'POST'])
def db():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
