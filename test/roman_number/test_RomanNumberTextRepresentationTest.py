# Numero 7
from roman_number.roman_number_text_representation import RomanNumberTextRepresentation


def test_001():
    assert "I" == RomanNumberTextRepresentation.of(1)


def test_002():
    assert "II" == RomanNumberTextRepresentation.of(2)


def test_003():
    assert "III" == RomanNumberTextRepresentation.of(3)


def test_004():
    assert "IV" == RomanNumberTextRepresentation.of(4)


def test_005():
    assert "V" == RomanNumberTextRepresentation.of(5)


def test_006():
    assert "VI" == RomanNumberTextRepresentation.of(6)


def test_007():
    assert "VII" == RomanNumberTextRepresentation.of(7)


def test_008():
    assert "VIII" == RomanNumberTextRepresentation.of(8)


def test_009():
    assert "IX" == RomanNumberTextRepresentation.of(9)


def test_010():
    assert "X" == RomanNumberTextRepresentation.of(10)


def test_011():
    assert "XI" == RomanNumberTextRepresentation.of(11)


def test_012():
    assert "XII" == RomanNumberTextRepresentation.of(12)


def test_013():
    assert "XIII" == RomanNumberTextRepresentation.of(13)


def test_014():
    assert "XIV" == RomanNumberTextRepresentation.of(14)


def test_015to018():
    assert RomanNumberTextRepresentation.of(15) == "XV"
    assert RomanNumberTextRepresentation.of(16) == "XVI"
    assert RomanNumberTextRepresentation.of(17) == "XVII"
    assert RomanNumberTextRepresentation.of(18) == "XVIII"


def test_019():
    assert "XIX" == RomanNumberTextRepresentation.of(19)


def test_020to029():
    assert RomanNumberTextRepresentation.of(20) == "XX"
    assert RomanNumberTextRepresentation.of(24) == "XXIV"
    assert RomanNumberTextRepresentation.of(26) == "XXVI"
    assert RomanNumberTextRepresentation.of(29) == "XXIX"

def test_030to039():
    assert RomanNumberTextRepresentation.of(30) == "XXX"
    assert RomanNumberTextRepresentation.of(34) == "XXXIV"
    assert RomanNumberTextRepresentation.of(36) == "XXXVI"
    assert RomanNumberTextRepresentation.of(39) == "XXXIX"

def test_040to049():
    assert RomanNumberTextRepresentation.of(40) == "XL"
    assert RomanNumberTextRepresentation.of(44) == "XLIV"
    assert RomanNumberTextRepresentation.of(46) == "XLVI"
    assert RomanNumberTextRepresentation.of(49) == "XLIX"


def test_050to089():
    assert RomanNumberTextRepresentation.of(50) == "L"
    assert RomanNumberTextRepresentation.of(69) == "LXIX"
    assert RomanNumberTextRepresentation.of(75) == "LXXV"
    assert RomanNumberTextRepresentation.of(78) == "LXXVIII"
    assert RomanNumberTextRepresentation.of(89) == "LXXXIX"

def test_090to099():
    assert RomanNumberTextRepresentation.of(90) == "XC"
    assert RomanNumberTextRepresentation.of(94) == "XCIV"
    assert RomanNumberTextRepresentation.of(96) == "XCVI"
    assert RomanNumberTextRepresentation.of(99) == "XCIX"


def test_100to999():
    assert RomanNumberTextRepresentation.of(100) == "C"
    assert RomanNumberTextRepresentation.of(224) == "CCXXIV"
    assert RomanNumberTextRepresentation.of(336) == "CCCXXXVI"
    assert RomanNumberTextRepresentation.of(407) == "CDVII"
    assert RomanNumberTextRepresentation.of(608) == "DCVIII"
    assert RomanNumberTextRepresentation.of(888) == "DCCCLXXXVIII"
    assert RomanNumberTextRepresentation.of(999) == "CMXCIX"
