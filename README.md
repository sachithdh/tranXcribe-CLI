# tranXcribe CLI

This is a CLI version of [tranXcribe webApp](https://github.com/sacheex/tranXcribe)

Transcribing audio files to text using openAI [Whisper](https://openai.com/research/whisper)
#### Supported audio formats - m4a, mp3, webm, mp4, mpga, wav, mpeg
Read FAQs [here](https://help.openai.com/en/articles/7031512-whisper-api-faq)


### INSTALLATION


```console
# clone the repo
$ git clone [https://github.com/sacheex/tranXcribe.git](https://github.com/sacheex/tranXcribe-CLI.git)

# navigate to the directory
$ cd tranXcribe-CLI

# install the requirements
$ python3 -m pip install -r requirements.txt
```


Generate [Openai API key](https://platform.openai.com/account/api-keys) and add it to the ```.env``` file.

``` console
OPENAI_API_KEY = "<add your OPENAI API KEY here>"
```


### USAGE AND OPTIONS


<!-- MANPAGE: BEGIN EXCLUDED SECTION -->
    python tranXcribe.py [OPTIONS]
<!-- MANPAGE: END EXCLUDED SECTION -->

#### General Options:

```
-h, --help                Print this help message and exit
-a PATH, --audio PATH     Path to audio file

```


