from contract_bridge.pocker import Card, NumberEnum, SuitEnum


def test_card_clubs_3():
    clubs_3 = Card(NumberEnum.THREE, SuitEnum.CLUBS)
    assert clubs_3.number == NumberEnum.THREE
    assert clubs_3.suit == SuitEnum.CLUBS
    assert clubs_3.rank == 3


def test_card_heart_ace():
    hearts_ace = Card(NumberEnum.ACE, SuitEnum.HEARTS)
    assert hearts_ace.number == NumberEnum.ACE
    assert hearts_ace.suit == SuitEnum.HEARTS
    assert hearts_ace.rank == 14
