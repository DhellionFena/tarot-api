"""
This module defines the settings configuration for the application.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Settings configuration for the application.

    Attributes:
        app_name (str): The name of the application.
        debug (bool): Flag to enable or disable debug mode.
    """

    app_name: str = "Tarot API"
    debug: bool = False

    class Config:
        """
        Configuration for the settings class.

        Attributes:
            env_file (str): The name of the environment file.
        """

        env_file = ".env"


settings = Settings()
