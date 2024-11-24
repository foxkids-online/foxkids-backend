from foxkids.domain.series import Series


def test_series():
    seria = Series(name="spider-man", count=20, current=1)
    assert seria.name == "spider-man"


def test_eq_series():
    seria1 = Series(name="spider-man", count=20, current=1)
    seria2 = Series(name="spider-man", count=21, current=2)
    assert seria1 == seria2


def test_increase_seria():
    seria = Series(name="spider-man", count=20, current=1)
    seria.increase_current_seria()
    assert seria.current == 2


def test_increase_last_seria():
    seria = Series(name="spider-man", count=20, current=20)
    seria.increase_current_seria()
    assert seria.current == 1


def test_to_dict():
    seria = Series(name="spider-man", count=20, current=20)
    assert {
        "count": 20,
        "current": 20,
        "name": "spider-man",
        "year": None,
        "genre": "",
        "name_rus": "",
        "description": "",
    } == seria.to_dict()
