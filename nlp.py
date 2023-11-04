from hugchat import hugchat
from hugchat.login import Login
from chat import get_answer

# Log in to huggingface and grant authorization to huggingchat
# sign = Login("Prajapatishailesh4941@gmail.com", "Shailesh4941")
# cookies = sign.login()

cookie_path_dir = "./cookies_snapshot"
# sign.saveCookiesToDir(cookie_path_dir)

sign = Login("Prajapatishailesh4941@gmail.com","Shailesh4941")
cookies = sign.loadCookiesFromDir(cookie_path_dir) #


# Create a ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  
chatbot.switch_llm(2)

def chatbot_answer(question):


    query,data = get_answer(question)
    query_result = chatbot.query(f'Craft one responses for this query "{query}" related to DTE Gujarats services without consistent introductory greetings. Ensure bot behavior by offering assistance and information. Elaborate on the organization quesitions only upon inquiry for DTE site detailed information.Encourage users to directly explore specific aspects of DTE Gujarats services using "we" pronouns.Please attempt to respond to a structured question without explicitly stating the query in your answer. this is data "{data}" ----give me answer only on greeting try to answer formated response')
    return query_result

    # print(query_result) 

# # stream response
# for resp in chatbot.query(
#     "Hello",
#     stream=True
# ):
#     print(resp)

# # Use web search (new feature)
# query_result = chatbot.query("Hi!", web_search=True)
# print(query_result) 
# for source in query_result.web_search_sources:
#     print(source.link)
#     print(source.title)
#     print(source.hostname)

# # Create a new conversation
# id = chatbot.new_conversation()
# chatbot.change_conversation(id)

# # Get conversation list
# conversation_list = chatbot.get_conversation_list()

# # Get the available models (not hardcore)
# models = chatbot.get_available_llm_models()

# # Switch model to the given index
# chatbot.switch_llm(0) # Switch to the first model
#  # Switch to the second model

# # Get information about the current conversation
# 

# # Get conversations on the server that are not from the current session (all your conversations in huggingchat)
# chatbot.get_remote_conversations(replace_conversation_list=True)

# # [DANGER] Delete all the conversations for the logged in user
# chatbot.delete_all_conversations()