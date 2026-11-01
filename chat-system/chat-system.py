# -------------------------------
# Message Class
# -------------------------------

class Message: 
  message_counter = 0

  def __init__(self,sender,content):
    self.sender = sender
    self.content = content

  def __str__(self):
    return f"Message from {self.sender.userName}: {self.content}"
    

# -------------------------------
# User Class
# -------------------------------


class User:
  def __init__(self,userName):
    self.userName = userName
    self.chatRoom = None

  def join_chatroom(self,chatroom):
     if self.chatRoom:
       print(f"{self.userName} is already in the chatroom")
     else:
        chatroom.add_user(self)
        self.chatRoom = chatroom
  
  def leave_chatroom(self):
      if not self.chatRoom:
         print(f"{self.userName} is not in any chatroom")
      else:
        print(f"{self.userName} has left {self.chatRoom.name}")
        self.chatRoom.remove_user(self)
        self.chatRoom = None
  
  def send_message(self,content):
      if not self.chatRoom:
         print(f"{self.userName} cannot send a message (not in any chatroom).")
      else:
        self.chatRoom.broadcast_message(self,content)

  def receive_message(self, message):
      print(f"{self.userName} received: {message}")
  

# -------------------------------
# ChatRoom Class
# -------------------------------

class ChatRoom:
  def __init__(self,name):
    self.name = name
    self.users = []
    self.messages = []

  def add_user(self,user):
    self.users.append(user)
    print(f"{user.userName} has joined {self.name}")
  
  def remove_user(self,user):
    self.users.remove(user)
    
  def broadcast_message(self,sender,content):
    message = Message(sender,content)
    self.messages.append(message)
    print(f"Message from {sender.userName}: {content}")
    for user in self.users:
      user.receive_message(message)
      

  def show_chat_history(self):
    print(f"\nChat History for {self.name}:")
    for msg in self.messages:
      print(msg)
      print("")


# ---------------------------------------
# Example Usage
# ---------------------------------------

if __name__ == "__main__":
 room = ChatRoom("Python Lounge")

 u1 = User("Abid")
 u2 = User("Ali")
 u3 = User("Khan")

 u1.join_chatroom(room)
 u2.join_chatroom(room)

 u1.send_message("Hello everyone!")
 u2.send_message("Hi Abid!")

 u3.join_chatroom(room)

 u3.send_message("Hey guys, what's up?")

 room.show_chat_history()

 u1.leave_chatroom()
 u2.leave_chatroom()
 u3.leave_chatroom()