
class RAGPrompt:
     def __init__(self, user_order, references):
        self.prompt = f"""
            User:
            - Please write me a twitter post with the given keywords:  {user_order}, using the writting style and the icons of these following tweets:
                - tweet1 with the context: {references['tweet 0']}
                - tweet2 with the context: {references['tweet 1']}
                - tweet3 with the context: {references['tweet 2']}
                - tweet4 with teh context: {references['tweet 3']}
                - tweet5 with the  context: {references['tweet 4']}
                - tweet6 with the context: {references['tweet 5']}
                - tweet7 with teh context: {references['tweet 6']}
                - tweet8 with the  context: {references['tweet 7']}

            Assitant:
                - Write your answer is in the commentary form and should only containt the twitter post content, nothing more:
                - Note: your tweet should follows a layout of these above 8 tweets, please create your own icons and hashtag for your tweets. 
            Start!
        """
        

class NormalPrompt:
    def __init__(self, user_order):
        self.prompt = f"""
            - Please execute the following user order
            - User order: Please write me a twitter post with keywords: {user_order}
            Write your answer in the commentary form:
            "answer": \n
            "your answer"
            Note: your answer should have 3 main parts: title, main content, ending part
            Start!
        """
