from dotenv import load_dotenv
import os

# loads the .env file and token
load_dotenv()


# gets the error messages from the .env file
def getErrorMessages() -> list[str]:
    # gets the number of error messages
    numberOfErrors: str | None = os.getenv("ERROR_MESSAGE_COUNT")

    # if the number of error messages is not found
    if not numberOfErrors:
        print("ERROR_MESSAGE_COUNT not found in .env file")
        return ["Something went wrong, please try again."]

    else:
        try:
            # gets the list of error messages
            numberOfErrorsInt: int = int(numberOfErrors)
            errorMessages: list[str] = []
            for i in range(numberOfErrorsInt):
                errorMessage: str | None = os.getenv(f"ERROR_MESSAGE_{i + 1}")
                if not errorMessage:
                    print(f"ERROR_MESSAGE_{i} not found in .env file")
                    return ["Something went wrong, please try again."]
                else:
                    errorMessages.append(errorMessage)

            return errorMessages
        except:
            print("ERROR_MESSAGE_COUNT is not a valid number")
            return ["Something went wrong, please try again."]
