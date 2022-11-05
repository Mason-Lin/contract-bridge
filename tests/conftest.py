import pytest

from contract_bridge.game import Game


@pytest.fixture(scope="function")
def game():
    return Game()
