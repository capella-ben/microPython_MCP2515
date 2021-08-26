from canio import Message, RemoteTransmissionRequest
from MCP2515 import MCP2515 as CAN
from time import sleep_ms

NODE_ID = 0x1234ABCD
#NODE_ID = 0xAA


can_bus = CAN(0, 5, baudrate = 25000, debug=True)
#print('Listening...')
i = 0
while True:
    with can_bus.listen(timeout=1.0) as listener:
        message = Message(id=NODE_ID, data=str(i).encode("utf-8"), extended=True)
        send_success = can_bus.send(message)
        print("Send success:", send_success)

        sleep_ms(1000)
        i = i + 1
        """
        message = Message(id=0xAAAA, data=str(i).encode("utf-8"), extended=True)
        send_success = can_bus.send(message)
        print("Send success:", send_success)

        sleep_ms(1000)
        i = i + 1
        """
        """
        message_count = listener.in_waiting()
        if message_count == 0:
            continue
        print(message_count, "messages available")
        for _i in range(message_count):
            msg = listener.receive()
            print("Message from ", hex(msg.id), "extended:", msg.extended)
            if isinstance(msg, Message):
                print("message data:", msg.data)
            if isinstance(msg, RemoteTransmissionRequest):
                print("RTR length:", msg.length)
            print("")
        """
