from converto.config import Configuration
from converto.converto import Converto
from converto.file_finder import FileFinder
from os import path, remove


output_files = ['flame.mp4', 'flame2.mp4', 'flame_ac.mp4', 'flame2_ac.mp4']


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
    assert len(menu_options) == 4


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


def test_convert_basic():
    # arrange
    clean_up_all_files()
    output_file = path.join(path.dirname(
        path.realpath(__file__)), "sample_files", "flame.mp4")
    conv = build_converto_action(0)
    # act
    conv._convert()
    # assert
    assert path.exists(output_file)
    clean_up_all_files()


def test_convert_with_multi_input():
    # arrange
    clean_up_all_files()
    output_file = get_full_output_file_path("flame2.mp4")
    conv = build_converto_action(1)
    # act
    conv._convert()
    # assert
    assert path.exists(output_file)
    clean_up_all_files()


def test_convert_with_formatting():
    # arrange
    clean_up_all_files()
    output_file = get_full_output_file_path("flame_ac.mp4")
    conv = build_converto_action(2)
    # act
    conv._convert()
    # assert
    assert path.exists(output_file)
    clean_up_all_files()
