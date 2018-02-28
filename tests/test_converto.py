from converto.config import Configuration
from converto.converto import Converto
from converto.file_finder import FileFinder
from os import path, remove

def build_converto():
    configuration = Configuration()
    conv = Converto(configuration, "test")
    conv.chosen_option = conv.config.options[0]
    return conv

def clean_up(output_file):
    try:
        remove(output_file)
    except:
        pass

def test_generate_menu_options():
    # arrange
    conv = build_converto()
    # act
    menu_options = conv._generate_menu_options()
    # assert
    assert len(menu_options) == 4

def test_get_output_filename():
    # arrange
    conv = build_converto()
    # act
    output_filename = conv._get_output_filename("test.avi", 0)
    # assert
    assert output_filename == "test.mp4"

def test_is_intermediary():
    # arrange
    conv = build_converto()
    # act
    is_intermediary = conv._is_intermediary(0)
    # assert
    assert is_intermediary == False

def test_convert():
    # arrange
    test_path = path.join(path.dirname(path.realpath(__file__)), "sample_files")
    output_file = path.join(path.dirname(path.realpath(__file__)), "sample_files", "flame.mp4")
    clean_up(output_file)
    conv = build_converto()
    file_finder = FileFinder(conv.config.options[0], "test")
    conv.files = file_finder._find_files_from_directory(test_path)    
    # act
    conv._convert()
    # assert
    assert path.exists(output_file)
