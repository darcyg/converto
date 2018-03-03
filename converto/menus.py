from __future__ import print_function
from builtins import input
from menu import Menu


def ask_user_for_files(valid_extension_list):
    print("Valid input types: {0}\n".format(valid_extension_list))
    return input("Enter the path of your file or directory of files: ").strip()


def create_choose_ffmpeg_command_menu(menu_options):
    main_menu = Menu(
        title="Choose which command you would like to run")
    main_menu.set_options(menu_options)
    return main_menu
