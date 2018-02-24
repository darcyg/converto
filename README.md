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

Configuration is done via an XML file. Here's an example:

```xml
<xml>
  <options>
    <option>
      <name>
        Create Access Copy
      </name>
      <valid-input-extensions>
        <ext>avi</ext>
        <ext>mov</ext>
      </valid-input-extensions>
      <commands>
        <command>
          <input-options></input-options>
          <output-options></output-options>
          <output-extension>
            mp4
          </output-extension>
        <command>
      <commands>
    </option>
  </options>
</xml>
```
