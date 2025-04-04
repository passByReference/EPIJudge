class RequestStatus(object):
    PENDING = 0
    ACCEPTED = 1
    REJECTED = 2

class Request(object):
    def __init__(self, sender, receiver):
        self.request_id = id(self)
        self.sender = sender
        self.receiver = receiver
        self.status = RequestStatus.PENDING # pending, accepted, rejected

    def accept(self):
        self.status = RequestStatus.ACCEPTED
        self.sender.add_friend(self.receiver)
        self.receiver.add_friend(self.sender)

    def reject(self):
        self.status = RequestStatus.REJECTED

    def __repr__(self):
        return f"Request from {self.sender} to {self.receiver} - Status: {self.status}"

class User(object):
    def __init__(self, user_name):
        self.user_name = user_name
        self.friends_list = set()
        self.requests = {}
        self.chats = {}
        self.inverse_chats = {}

    def add_friend(self, friend):
        if isinstance(friend, User) and friend not in self.friends_list:
            if friend == self:
                raise ValueError("Cannot add yourself as a friend")
            self.friends_list.add(friend)

    def add_friend_request(self, friend):
        print(f"{self.user_name} adds friend {friend.user_name}")
        if isinstance(friend, User) and friend not in self.friends_list:
            if friend == self:
                raise ValueError("Cannot add yourself as a friend")
            request = Request(self, friend)
            self.requests[request.request_id] = request
            friend.requests[request.request_id] = request
        else:
            raise ValueError("Friend must be an instance of User")
    
    def remove_friend(self, friend):
        if isinstance(friend, User) and friend in self.friends_list:
            self.friends_list.remove(friend)
        else:
            raise ValueError("Friend must be an instance of User")
        
    def create_chat(self, group=False):
        if group:
            chat = GroupChat()
        else:
            chat = Chat()
        chat.chat_users.add(self)
        self.chats[chat.chat_id] = chat
        return chat
    

    
    def send_message(self, chat_id, message):
        if chat_id in self.chats:
            self.chats[chat_id].messages[self.user_name] = message
        else:
            raise ValueError("Chat not found")
        
    def view_messages(self, chat_id):
        if chat_id in self.chats:
            return self.chats[chat_id].messages
        else:
            raise ValueError("Chat not found")
        

    def invite(self, chat_id, user):
        if chat_id in self.chats:
            chat = self.chats[chat_id]
            if isinstance(chat, GroupChat):
                chat.invite(self, user)
            elif isinstance(chat, Chat):
                print(f"Inviting {user.user_name} to chat {chat_id}")
                if user in self.friends_list:
                    chat.add_user(user)
                    self.inverse_chats[user.user_name] = chat_id

                    user.inverse_chats[self.user_name] = chat_id
                    user.chats[chat_id] = chat
                    
                else:
                    self.add_friend(user)
                    print(f"Request sent to {user.user_name} to join chat")
        else:
            raise ValueError("Chat not found")
    
    def accept_request(self, request_id):
        print(f"{self.user_name} accepted request {request_id}")
        if request_id in self.requests:
            self.requests[request_id].accept()
            del self.requests[request_id]
        else:
            raise ValueError("Request not found")
    
    def reject_request(self, request_id):
        if request_id in self.requests:
            self.requests[request_id].reject()
            del self.requests[request_id]
        else:
            raise ValueError("Request not found")
    
    

class Chat(object):
    def __init__(self):
        self.chat_id = id(self)
        self.chat_users = set()
        self.messages = {}

    def add_user(self, user):
        if isinstance(user, User):
            self.chat_users.add(user)
        else:
            raise ValueError("User must be an instance of User")
    def remove_user(self, user):
        if isinstance(user, User) and user in self.chat_users:
            self.chat_users.remove(user)
        else:
            raise ValueError("User must be an instance of User")

    def __repr__(self):
        return self.chat_id
    
class GroupChat(Chat):
    def __init__(self):
        super().__init__()
        
    def invite(self, user, invitee):
        if isinstance(user, User) and isinstance(invitee, User):
            if user not in self.chat_users:
                raise ValueError("User not in chat")
            if invitee in self.chat_users:
                raise ValueError("User already in chat")
            print(f"{user.user_name} invited {invitee.user_name} to chat {self.chat_id}")
            self.chat_users.add(invitee)
            invitee.chats[self.chat_id] = self
        else:
            raise ValueError("User must be an instance of User")

def main():
    user_1 = User("Alice")
    user_2 = User("Bob")
    user_3 = User("Charlie")
    user_4 = User("Dave")
    chats = [user_1.create_chat(), user_2.create_chat(group=True), user_3.create_chat(), user_4.create_chat()]
    user_1.add_friend_request(user_2)
    user_2.accept_request(list(user_2.requests.values())[0].request_id)
    user_1.invite(chats[0].chat_id, user_2)
    user_1.send_message(chats[0].chat_id, "Hello Bob!")
    print(user_1.view_messages(chats[0].chat_id))

    user_2.send_message(chats[0].chat_id, "Hello Alice!")
    print(user_2.view_messages(chats[0].chat_id))

    user_2.invite(chats[1].chat_id, user_3)
    user_2.invite(chats[1].chat_id, user_4)
    user_2.send_message(chats[1].chat_id, "Hello Charlie and Dave!")
    print(user_2.view_messages(chats[1].chat_id))
    user_3.send_message(chats[1].chat_id, "Hello Bob!")
    print(user_3.view_messages(chats[1].chat_id))
    user_4.send_message(chats[1].chat_id, "Hello Bob!")
    print(user_4.view_messages(chats[1].chat_id))



if __name__ == "__main__":
    main()
