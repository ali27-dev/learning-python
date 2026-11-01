# Chat System

A small Python OOP demo of a chat room. Users can join a room, send messages, receive broadcasts, view history, and leave.

## Run

```bash
python3 chat-system.py
```

Requires Python 3. No extra packages.

## How it works

| Class | Role |
| --- | --- |
| `User` | Join / leave a room, send and receive messages |
| `ChatRoom` | Keep the user list, broadcast messages, store history |
| `Message` | One chat message (`sender` + `content`) |

Flow:

1. Create a `ChatRoom` and some `User` objects.
2. Users join the room with `join_chatroom()`.
3. `send_message()` asks the room to `broadcast_message()`.
4. Every user in the room gets `receive_message()`.
5. `show_chat_history()` prints all stored messages.

A user can only be in one room at a time. Sending a message while not in a room prints an error.

## Example

```python
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
```

## Sample output

```text
Abid has joined Python Lounge
Ali has joined Python Lounge
Message from Abid: Hello everyone!
Abid received: Message from Abid: Hello everyone!
Ali received: Message from Abid: Hello everyone!
Message from Ali: Hi Abid!
Abid received: Message from Ali: Hi Abid!
Ali received: Message from Ali: Hi Abid!
Khan has joined Python Lounge
Message from Khan: Hey guys, what's up?
Abid received: Message from Khan: Hey guys, what's up?
Ali received: Message from Khan: Hey guys, what's up?
Khan received: Message from Khan: Hey guys, what's up?

Chat History for Python Lounge:
Message from Abid: Hello everyone!

Message from Ali: Hi Abid!

Message from Khan: Hey guys, what's up?

Abid has left Python Lounge
Ali has left Python Lounge
Khan has left Python Lounge
```
