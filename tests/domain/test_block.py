from foxkids.domain import Block, Series


def test_block_to_json():
    indiana = Series(name="indiana", current=1, count=10)
    block = Block(
        weekday=0,
        name="foxkids",
        index_in_weekday=0,
        series_list=[indiana, indiana],
    )
    assert block.to_dict() == {
        "name": "foxkids",
        "weekday": 0,
        "index_in_weekday": 0,
        "series_list": ["indiana", "indiana"],
    }
