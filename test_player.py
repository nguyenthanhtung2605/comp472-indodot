import player


class TestCalculator:

    def test_addition(self):
        assert 4 == player.move_left(2, 2)

    def test_subtraction(self):
        assert 2 == player.move_right(4, 2)