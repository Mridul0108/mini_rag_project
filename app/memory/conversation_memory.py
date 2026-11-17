
class ConversationMemory:

    def __init__(self, max_messages=50):
        self.messages = []
        self.max_messages = max_messages

    def add_message(self, role, content):
        message = {
            "role": role,
            "content": content
        }

        self.messages.append(message)

        
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]

    def get_history(self):
        return self.messages.copy()

    def clear_history(self):
        self.messages.clear()
