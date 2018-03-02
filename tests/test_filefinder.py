from __future__ import print_function
from converto.file_finder import FileFinder
from converto.config import Configuration
from converto.converto import Converto
from os import path

def build_file_finder():
    configuration = Configuration()
    conv = Converto(configuration, "test")
    file_finder = FileFinder(conv.config.options[0], "test")
    return file_finder

def test_clean_user_input():
    # arrange
    file_finder = build_file_finder()
    # act
    cleaned_input = file_finder._clean_user_input("test\ input")
    # assert
    assert cleaned_input == "test input"

def test_find_files_from_directory():
    # arrange
    file_finder = build_file_finder()
    test_path = path.join(path.dirname(path.realpath(__file__)), "sample_files")
    # act
    found_files = file_finder._find_files_from_directory(test_path)
    # assert
    assert len(found_files) == 2

def test_get_file_list():
    # arrange
    file_finder = build_file_finder()
    test_path = path.join(path.dirname(path.realpath(__file__)), "sample_files")
    file_finder.files = file_finder._find_files_from_directory(test_path)
    # act
    file_list_string = file_finder._get_file_list()
    # assert
    assert len(file_list_string.split('\n')) == 3

def test_get_exts_list():
    # arrange
    file_finder = build_file_finder()
    # act
    ext_list_string = file_finder._get_exts_list()
    # assert
    assert ext_list_string == "avi"

def test_file_is_right_extension():
    # arrange
    file_finder = build_file_finder()
    # act
    is_valid = file_finder._file_is_right_extension("test.avi")
    # assert
    assert is_valid

def test_build_menu_title():
    # arrange
    configuration = Configuration()
    conv = Converto(configuration, "test")
    command_list = conv._generate_command_list()
    file_finder = FileFinder(conv.config.options[0], "test")
    # act
    menu_title = file_finder._build_menu_title(command_list)
    # assert
    assert menu_title is not None