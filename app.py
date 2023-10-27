import os
from flask import Flask,render_template
from embedchain import App

os.environ["HUGGINGFACE_ACCESS_TOKEN"] = "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"
app = Flask(__name__)


@app.route('/')
def hello():
    return "hello world"


if __name__ == "__main__":
    app.run(debug=True)

# app = App.from_config(yaml_path="huggingface.yaml")

# app.add("https://dte.gujarat.gov.in/dte-team")
# app.add("https://dte.gujarat.gov.in/recent-update")

# while(True):
#     question = input("Enter question: ")
#     if question in ['q', 'exit', 'quit']:
#         break
#     answer = app.query(question)
#     print(answer)