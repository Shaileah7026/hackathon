import os
from embedchain import App as EmbedchainApp  # Rename the 'app' variable here

os.environ["HUGGINGFACE_ACCESS_TOKEN"] = "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"

# Create an instance of the EmbedchainApp
embedchain_app = EmbedchainApp.from_config(yaml_path="huggingface.yaml")

embedchain_app.add("https://dte.gujarat.gov.in/dte-team")
embedchain_app.add("https://dte.gujarat.gov.in/recent-update")

def get_answer(question):
    try:
        answer = embedchain_app.query(question)  
        return answer
    except Exception as e:
        return f"An error occurred: {str(e)}"

