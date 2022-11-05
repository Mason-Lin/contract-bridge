from contract_bridge.user import User


def test_user_name():
    mason = User("mason")
    assert mason.name == "mason"
