# Converto

## Summary

Converto acts as a human-friendly wrapper around FFmpeg and also provides some productivity-enhancing features.

## Features

* Batch Processing

* FFmpeg command-chaining

* Configurable


## Requirements

* [Python 2.7](https://www.python.org/) must be installed.

* [FFmpeg](https://ffmpeg.org/) must be on your path

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

The above configuration get interpreted as this ffmpeg command:

```shell
ffmpeg -i input.avi -vcodec h264 -acodec aac -strict -2 input.mp4
```

Where "input.avi" is a file that the user chose to be operated on.
