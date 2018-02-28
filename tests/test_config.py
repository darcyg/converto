from converto.config import Configuration


def test_find_config():
    # arrange
    config_file_path = None
    # act
    config = Configuration(config_file_path)
    # assert
    assert config.config_file_path != None


def test_repr():
    # arrange
    config_file_path = None
    # act
    config = Configuration(config_file_path)
    print(config)
    # assert
    assert True
