from converto.config import Configuration


def test_find_config():
    # arrange
    config_file_path = None
    # act
    config = Configuration(config_file_path)
    # assert
    assert config.config_file_path != None


def test_find_config_fail():
    # arrange
    config_file_path = "does_not_exist.json"
    expected_behavior = False
    # act
    try:
        config = Configuration(config_file_path)
    except:
        expected_behavior = True
    # assert
    assert expected_behavior


def test_repr():
    # arrange
    config_file_path = None
    # act
    config = Configuration(config_file_path)
    print(config)
    # assert
    assert True
