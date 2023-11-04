import os
from embedchain import App as EmbedchainApp  # Rename the 'app' variable here

os.environ["HUGGINGFACE_ACCESS_TOKEN"] = "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"

# Create an instance of the EmbedchainApp
embedchain_app = EmbedchainApp.from_config(yaml_path="huggingface2.yaml")

embedchain_app.add("https://dte.gujarat.gov.in/dte-team")
embedchain_app.add("https://dte.gujarat.gov.in/vision")


while(True):
        question = input("Enter question :")
        answer = embedchain_app.query(question)  
        print(answer)

