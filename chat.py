from hugchat import hugchat
from hugchat.login import Login
import os
from embedchain import App as EmbedchainApp  # Rename the 'app' variable here

os.environ["HUGGINGFACE_ACCESS_TOKEN"] = "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"

# Create an instance of the EmbedchainApp
embedchain_app = EmbedchainApp.from_config(yaml_path="huggingface.yaml")


embedchain_app.add("https://github.com/Shaileah7026/Remini-clone/blob/main/sitemap.xml",data_type = 'sitemap')

cookie_path_dir = "./cookies_snapshot"
# sign.saveCookiesToDir(cookie_path_dir)
#sign in into hugginface
sign = Login("Prajapatishailesh4941@gmail.com","Shailesh4941")
cookies = sign.loadCookiesFromDir(cookie_path_dir) #
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  

def get_answer(question):
    try:
        answer = embedchain_app.query(question)  
        return chatbot_answer(answer,question)
    except Exception as e:
        return f"An error occurred: {str(e)}"

def chatbot_answer(data,query):
   
    query_result = chatbot.query(f'Craft one responses for this query "{query}" related to DTE Gujarats services without consistent introductory greetings. Ensure bot behavior by offering assistance and information. Elaborate on the organization quesitions only upon inquiry for DTE site detailed information.Encourage users to directly explore specific aspects of DTE Gujarats services using "we" pronouns.Please attempt to respond to a structured question without explicitly stating the query in your answer. this is data "{data}" ----give me answer only on greeting try to answer formated response')
    return query_result    


# print(get_answer("what is current commissionr of DTE"))

# while(True):
#     question = input("Enter question :")
#     answer = embedchain_app.query(question)
#     print(answer)