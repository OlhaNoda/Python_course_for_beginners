# task3_110121
"""
Task 3
TV controller
Create a simple prototype of a TV controller in Python. It’ll use the following commands:
first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes",
if the channel N or 'name' exists in the list, or "No" - in the other case.
The default channel turned on before all commands is №1.
Your task is to create the TVController class and methods described above.
"""

CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:

    def __init__(self, channels):
        self.channels = channels
        self.channel_index = 0

    def first_channel(self):
        self.channel_index = 0
        return self.current_channel()

    def last_channel(self):
        self.channel_index = len(self.channels) - 1
        return self.current_channel()

    def turn_channel(self, number):
        self.channel_index = number - 1
        return self.current_channel()

    def next_channel(self):
        if self.channel_index != len(self.channels)-1:
            self.channel_index += 1
        else:
            self.channel_index = 0
        return self.current_channel()

    def previous_channel(self):
        if self.channel_index != 0:
            self.channel_index -= 1
        else:
            self.channel_index = len(self.channels) - 1
        return self.current_channel()

    def current_channel(self):
        return self.channels[self.channel_index]

    def is_exist(self, search_channel):
        if search_channel in range(1, len(self.channels)+1) or search_channel in self.channels:
            answer = 'Yes'
        else:
            answer = 'No'
        return answer


if __name__ == "__main__":
    controller = TVController(CHANNELS)
    print(controller.first_channel())
    print(controller.last_channel())
    print(controller.turn_channel(1))
    print(controller.next_channel())
    print(controller.previous_channel())
    print(controller.current_channel())
    print(controller.is_exist(4))
    print(controller.is_exist('BBC'))
