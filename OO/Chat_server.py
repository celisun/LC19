# functionality requirement
# user: add, remove a user, add or remove to a user's friends list with fridn reques
# create a group chat: invite to a group chat, post message to a group chat
# create 1-1 chat: invite a friend to, post a message to private chat
# no need to worry about scaling initially

from abc import ABCMeta

class UserService:
    def __init__(self):
        self.users_by_id = {}

    def add_user(self, user_id, name, pass_hash):
    def remove_user(self, user_id):
    def add_friend_request(self, from_user_id, to_user_id):
    def approve_friend_request(self, from_user_id, to_user_id):
    def reject_friend_request(self, from_user_id, to_user_id):

class User:
    def __init__(self, user_id, name, pass_hash):
        self.user_id = user_id
        self.name = name
        self.pass_hash = pass_hash
        self.friends_by_id = {}
        self.friends_ids_to_private_chats = {}  # friend id, private chat
        self.group_chats_by_id = {}    # chat id, group chats
        self.received_friend_request_by_friend_id = {}  # friend_id, add_request
        self.sent_friend_request_by_friend_id = {} # friend_id, add_request

    def message_user(self, friend_id, message):
    def message_group(self, group_id, message):
    def send_friend_request(self, friend_id):
    def receive_friend_request(self, friend_id):
    def approve_friend_request(self, friend_id):
    def reject_friend_requeset(self, friend_id):

class Chat(metaclass=ABCMeta):
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.users = []
        self.messages = []

class PrivateChat(Chat):
    def __init__(self, first_user, other_user):
        super(PrivateChat, self).__init__()
        self.users.append(first_user)
        self.users.append(other_user)

class GroupChat(Chat):
    def add_user(self, user):
    def remove_user(self, user):


class Message:
    def __init__(self, message_id, message, timestamp):
        self.message_id = message_id
        self.message = message
        self.timestamp = timestamp

class AddRequest:
    def __init__(self, from_user_id, to_user_id, request_status, timestamp):
        self.from_user_id = from_user_id
        self.to_user_id = to_user_id
        self.request_status = request_status
        self.timestamp = timestamp

class RequestStatus(Enum):
    UNREAD = 0
    READ = 1
    ACCEPTED = 2
    REJECT = 3