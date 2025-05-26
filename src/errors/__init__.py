import errors.error_messages as error_messages
import random


# import error messages
errors = error_messages.getErrorMessages()


# gets a random error message from the list
def getErrorMessage():
    return random.choice(errors)
