from source.channel import Channel


def test_channel():
    moscow_python = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    classic_music = Channel('UCl5Iupsbi7GzmVX3PK6-SEQ')
    teremok_sounds = Channel('UCgAZFXXLy6tQXNXz-omrS-A')

    assert moscow_python.print_info()
    assert classic_music.print_info()
    assert teremok_sounds.print_info()

test_channel()