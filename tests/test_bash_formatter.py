from foxkids.utils.bash_formatter import create_curl, create_program_row


def test_create_program_row():
    assert (
        create_program_row(path="src/foxkids/andy/1.mp4")
        == "ffmpeg  -re -i src/foxkids/andy/1.mp4 -c:a aac -c:v libx264 -b:v 200k -b:a 64K -r 25 -s 320x240 -f flv rtmp://server_rtmp:1935/stream/test\n"  # noqa: E501
    )


def test_create_curl():
    assert (
        create_curl("andy", "luie")
        == 'curl -X POST http://127.0.0.1/api/current_series/ -H "Content-Type: application/json" -d \'{"current_series": "andy", "next_series": "luie"}\'\n'  # noqa: E501
    )
