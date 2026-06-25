import pytest
from config.enviroment import (SAUCE_STANDARD_USERNAME,SAUCE_PASSWORD)

@pytest.fixture
def credentials():
    username=SAUCE_STANDARD_USERNAME
    password=SAUCE_PASSWORD
    return [username,password]