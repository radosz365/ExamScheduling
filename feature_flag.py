from flagsmith import Flagsmith
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".venv/.env")

flagsmith_api_key = os.getenv("FLAGSMITH_API_KEY")
if not flagsmith_api_key:
    raise ValueError("FLAGSMITH_API_KEY is not set in the .env file")

flagsmith = Flagsmith(environment_key=flagsmith_api_key)


def get_flag_value(flag_name, default_value=None):
    """
    Retrieves the value of a flag from Flagsmith. If an error occurs, returns the default value.

    :param flag_name: The name of the flag
    :param default_value: The default value to return if the flag is not available
    :return: The flag's value (boolean) or the default value
    """
    try:
        flags = flagsmith.get_environment_flags()
        for flag in flags.all_flags():
            if flag.feature_name == flag_name:
                return flag.enabled
        print(f"Flag '{flag_name}' not found. Using default value.")
        return default_value
    except Exception as e:
        print(f"Error fetching flag '{flag_name}': {e}")
        return default_value
