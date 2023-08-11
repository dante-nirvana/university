# Importing packages and modules

import code.Cat # importing the module CAT from package CODE


new_cat = code.Cat.Cat(age=10, height=30, weight=4.5, position=(0, 0), fur= 'long',
                        breed='orange',  tail_fur='short')
new_cat.move_x()


# from code.Cat import Cat # importing only the class


# new_cat: Cat = Cat(age=10, height=30, weight=4.5, position=(0, 0), fur= 'long',
#                     breed='orange',  tail_fur='short')
# new_cat.move_x()

