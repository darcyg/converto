from converto.config import Configuration
from converto.converto import Converto
from converto.file_finder import FileFinder
from os import path, remove


output_files = [
    'flame.mp4',
    'flame2.mp4',
    'flame_ac.mp4',
    'flame2_ac.mp4',
    'flame_roundtrip.avi',
    'flame2_roundtrip.avi'
]


def build_converto(option_number):
    configuration = Configuration()
    conv = Converto(configuration, "test")
    conv.chosen_option = conv.config.options[option_number]
    return conv


def build_converto_action(option_number):
    clean_up_all_files()
    test_path = path.join(path.dirname(
        path.realpath(__file__)), "sample_files")
    conv = build_converto(option_number)
    file_finder = FileFinder(conv.config.options[option_number], "test")
    conv.files = file_finder._find_files_from_directory(test_path)
    conv.command_list = conv._generate_command_list()
    return conv


def get_full_output_file_path(filename):
    return path.join(path.dirname(
        path.realpath(__file__)), "sample_files", filename)


def clean_up_all_files():
    for f in output_files:
        output_file = get_full_output_file_path(f)
        clean_up(output_file)


def clean_up(output_file):
    try:
        remove(output_file)
    except:
        pass


def test_generate_menu_options():
    # arrange
    conv = build_converto(0)
    # act
    menu_options = conv._generate_menu_options()
    # assert
    assert len(menu_options) == 6


def test_get_output_filename():
    # arrange
    conv = build_converto(0)
    # act
    output_filename = conv._get_output_filename("test.avi", 0)
    # assert
    assert output_filename == "test.mp4"


def test_is_intermediary():
    # arrange
    conv = build_converto(0)
    # act
    is_intermediary = conv._is_intermediary(0)
    # assert
    assert is_intermediary == False


def test_generate_command_list():
    # arrange
    conv = build_converto_action(0)
    # act
    command_list = conv._generate_command_list()
    # assert
    assert(len(command_list) == 2)


def test_convert_basic():
    # arrange
    clean_up_all_files()
    output_file = get_full_output_file_path("flame.mp4")
    conv = build_converto_action(0)
    # act
    conv.convert()
    # assert
    assert path.exists(output_file)
    clean_up_all_files()


def test_convert_with_multi_input():
    # arrange
    clean_up_all_files()
    output_file_1 = get_full_output_file_path("flame.mp4")
    output_file_2 = get_full_output_file_path("flame2.mp4")
    conv = build_converto_action(1)
    # act
    conv.convert()
    # assert
    try:
        assert path.exists(output_file_1)
    except:  # since we can't control how the OS discovers files, check both names
        assert path.exists(output_file_2)
    clean_up_all_files()


def test_convert_with_formatting():
    # arrange
    clean_up_all_files()
    output_file = get_full_output_file_path("flame_ac.mp4")
    conv = build_converto_action(2)
    # act
    conv.convert()
    # assert
    assert path.exists(output_file)
    clean_up_all_files()


def test_convert_multi_step():
    # arrange
    clean_up_all_files()
    output_file_1 = get_full_output_file_path("flame_roundtrip.avi")
    output_file_2 = get_full_output_file_path("flame2_roundtrip.avi")
    conv = build_converto_action(3)
    # act
    conv.convert()
    # assert
    try:
        assert path.exists(output_file_1)
    except:  # since we can't control how the OS discovers files, check both names
        assert path.exists(output_file_2)
    clean_up_all_files()


def test_convert_with_wildcard():
    # arrange
    clean_up_all_files()
    output_file = get_full_output_file_path("flame.avi")
    conv = build_converto_action(4)
    conv.files = [output_file]
    conv.command_list = conv._generate_command_list()
    # act
    conv.convert()
    # assert
    assert path.exists(output_file)
    clean_up_all_files()
