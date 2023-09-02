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

# import sched
# import time
# from sched import scheduler


# # callback function
# def show_message(message: str) -> None:
#     print(message)


# def event_scheduler(scheduler: sched.scheduler, interval: float, message: str) -> None:
#     # scheduling next event
#     scheduler.enter(interval, 1, event_scheduler, (scheduler, interval, message))
#     show_message(message)


# # instantiating a new scheduler
# new_scheduler: scheduler = sched.scheduler(time.time, time.sleep)

# # scheduling the first event
# event_scheduler(new_scheduler, 1, "scheduled message with 1 second interval")

# print('waiting to display scheduled messages...')

# # running scheduler on a loop (ctrl + c to interrupt manually)
# new_scheduler.run()

# 4.2.1 Decorators

# how to create new decorators

# def my_decorator(function: Any):
#     def wrapper():
#         print('Start')
#         function()
#         print('End')
#     return wrapper


# # applying the decorator
# @my_decorator
# def my_function():
#     print('Executing my function.')


# # calling decorated function
# my_function()


# 4.2.1.2
# import time
# from typing import Any

# def function_timer(func: Any):
#     def wrapper(*args, **kwargs):
#         start: float = time.time()
#         results: any = func(*args, **kwargs)
#         end: float = time.time()
#         print(f"Function '{func.__name__}' executed in {end - start:.4f} seconds")
#         return results
#     return wrapper


# # applying decorator
# @function_timer
# def my_function(waiting_time: float) -> None:
#     time.sleep(waiting_time)
#     print('Executing my function')


# # calling decorated function
# my_function(2)
# print('\n\n')

# 4.2.2 class decorators

# from typing import Any


# class Car:
#     def __init__(self, decorated_class) -> None:
#         self.decorated_class = decorated_class

#     def __call__(self, *args: Any, **kwargs: Any) -> Any:
#         # original class instance
#         class_instance: Any = self.decorated_class(*args, **kwargs)
#         # new attribute
#         class_instance.wheels: int = 4
#         return class_instance
    

# @Car
# class Automobile:
#     def __init__(self, model: str) -> None:
#         self.model = model


# # instantiating a decorated class
# new_auto: Automobile = Automobile('Civic')

# # showing attributes
# print(f"Model: {new_auto.model}")
# print(f"Number of wheels: {new_auto.wheels}\n\n")


# 4.3 - List Comprehensions

# import time
# from typing import Any

# def function_timer(func: Any):
#     def wrapper(*args, **kwargs):
#         start: float = time.time()
#         results: any = func(*args, **kwargs)
#         end: float = time.time()
#         print(f"Function '{func.__name__}' executed in {end - start:.4f} seconds")
#         return results
#     return wrapper


# @function_timer
# def even_numbers_simple(max_value: int) -> list:
#     list_even: list = list()
#     for num in range(max_value):
#         if num % 2 == 0:
#             list_even.append(num)
#     return list_even


# @function_timer
# def even_numbers_comprehension(max_value: int) -> list:
#     list_even: list = [num for num in range(max_value) if num % 2 == 0]
#     return list_even


# even_numbers_simple(100000000)
# even_numbers_comprehension(100000000)
# print('\n\n')


# # 4.4 - Design Patterns - Behavioral Patterns

# # Mediator

# from code.Mediator import ControlTower
# from code.Mediator import Plane


# # instantiating a new tower
# control_tower: ControlTower = ControlTower()

# # instantiating planes
# plane1: Plane = Plane("Plane1")
# plane2: Plane = Plane("Plane2")
# plane3: Plane = Plane("Plane3")

# # adding planes to the tower
# control_tower.add_plane(plane1)
# control_tower.add_plane(plane2)
# control_tower.add_plane(plane3)

# # exchanging messages 
# plane1.send_message("Let's take off!")
# plane2.send_message("Ready to take off.")
# plane3.send_message("awaiting instructions.")

# 4.5 - Design Pattern - Creational Patterns

# Observer

from code.Observer import Messenger
from code.Observer import User
from code.Observer import Group


messenger: Messenger = Messenger()

# instantiating users
user1: User = User("Alice")
user2: User = User("Bob")
user3: User = User("Charlie")

# instantiating groups
group1: Group = Group("Family")
group2: Group = Group("Work")


# adding observers to the messenger
messenger.add_observer(user1)
messenger.add_observer(user2)
messenger.add_observer(user3)

# adding members to the groups
group1.add_member(user1)
group1.add_member(user2)

group2.add_member(user2)
group2.add_member(user3)

# sending messages
messenger.notify_observers("Admin", "Welcome to our messenger app!")
group1.receive_notification("Admin", "New family meeting scheduled for tomorrow")
user3.receive_notification("Alice", "Hi! How are you?")
