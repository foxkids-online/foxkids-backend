from foxkids.domain import Block, Series


def test_block_to_json():
    indiana = Series(name="indiana", current=1, count=10)
    block = Block(
        weekday=0,
        name="foxkids",
        index_in_weekday=0,
        series_list=[indiana, indiana],
    )
    print(block.to_dict())
    print(block)
    assert block.to_dict() == {
        "name": "foxkids",
        "weekday": 0,
        "index_in_weekday": 0,
        "series_list": [
            {
                "name": "indiana",
                "count": 10,
                "current": 1,
                "year": None,
                "genre": "",
                "name_rus": "",
                "description": "",
            },
            {
                "name": "indiana",
                "count": 10,
                "current": 1,
                "year": None,
                "genre": "",
                "name_rus": "",
                "description": "",
            },
        ],
    }
