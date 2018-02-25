# converto

## Requirements

* [Python 2.7](https://www.python.org/) must be installed.

* ffmpeg must be on your path. open a terminal and type `ffmpeg`. If that brought up a bunch of options, you can continue to the "Installation" section.

  **OSX**: `brew install ffmpeg`

  **Windows**: download ffmpeg and place installation directory in your PATH environment variable

## Installation

* Download this repo

* Unzip

* run `python setup.py install`

* To confirm installation succeded, run `converto`

## Configuration

Configuration is done via a JSON file. Here's an example:

```json
{
  "options": [
    {
      "name": "Create Access Copy",
      "valid-input-extensions": [
        "avi",
        "mov"
      ],
      "commands": [
        {
          "input-options": "",
          "output-options": "-vcodec h264 -acodec aac -strict -2",
          "output-extension": "mp4"
        }
      ]
    }
  ]
}
```
