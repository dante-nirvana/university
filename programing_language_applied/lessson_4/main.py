# # 4.1.1 Keyboard events
# import keyboard


# def on_key_event(event: keyboard._Event) -> None:  # callback function
#     if event.event_type == keyboard.KEY_DOWN:  # verifying pressed key
#         print(f'key pressed: {event.name}')
#         if event.name == 'a':
#             print("key 'a' pressed.")


# keyboard.on_press(on_key_event) # hooking

# try:
#     while True:
#         pass
# except KeyboardInterrupt:
#     raise KeyboardInterrupt

# 4.1.2 Time events

import sched
import time
from sched import scheduler


# callback function
def show_message(message: str) -> None:
    print(message)


def schedule_event(scheduler, interval, message):
    # scheduling next event
    scheduler.enter(interval, 1, schedule_event, (scheduler, interval, message))
    show_message(message)


# instantiating a new scheduler
new_scheduler: scheduler = sched.scheduler(time.time, time.sleep)

# scheduling the first event
schedule_event(new_scheduler, 1, "scheduled message with 1 second interval")

print('waiting to display scheduled messages...')

# running scheduler on a loop (ctrl + c to interrupt manually)
new_scheduler.run()
