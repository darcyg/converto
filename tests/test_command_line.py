from converto.command_line import parse_args, setup_logging
import logging


def test_parse_args():
    # act
    args = parse_args()
    # assert
    assert args.config == None
    assert args.debug == False
    assert args.input == None


def test_setup_logging():
    # act
    setup_logging(False)
    setup_logging(True)
    # assert
    assert True
