from dotenv import load_dotenv
import os


# loads the .env file and token
load_dotenv()


# validates the error message count from the .env file
def validate_error_message_count(errorMessageCount):

    # if the number of error messages is not found
    if not errorMessageCount:
        raise ValueError("ERROR_MESSAGE_COUNT not found in .env file")

    # if the number of error messages is not a number
    if not errorMessageCount.isdigit():
        raise ValueError("ERROR_MESSAGE_COUNT is not a valid number")

    # if the number of error messages is less than 1
    if int(errorMessageCount) < 1:
        raise ValueError("ERROR_MESSAGE_COUNT must be at least 1")

    return int(errorMessageCount)


# validates a single error message from the .env file
def validate_error_message(errorMessage, index):

    # if the error message is not found
    if not errorMessage:
        raise ValueError(f"ERROR_MESSAGE_{index} not found in .env file")

    # if the error message is empty
    if not errorMessage.strip():
        raise ValueError(f"ERROR_MESSAGE_{index} is empty in .env file")

    # if the error message is too long
    if len(errorMessage) > 200:
        raise ValueError(f"ERROR_MESSAGE_{index} must be less than 200 characters")

    return errorMessage


# gets the error messages from the .env file
def getErrorMessages():

    # gets the number of error messages
    errorMessageCount = os.getenv("ERROR_MESSAGE_COUNT")
    count = validate_error_message_count(errorMessageCount)

    # gets the list of error messages
    errorMessages = []
    for i in range(count):

        errorMessage = os.getenv(f"ERROR_MESSAGE_{i + 1}")
        validated_message = validate_error_message(errorMessage, i + 1)

        # adds the error message to the list
        errorMessages.append(validated_message)

    return errorMessages
