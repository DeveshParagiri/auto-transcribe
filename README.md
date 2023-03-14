# Autotranscribe

Autotranscribe is a simple library to convert video/audio to text. The library currently supports transcription of youtube files as well as implementing multiprocessing for faster transcription. It is built around the OpenAI whisper model.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install autotranscribe.

```bash
pip install autotranscribe
```

## Usage

```python
import autotranscribe

# Transcribe a youtube file with basic functionality.
autotranscribe.transcribe_from_youtube(url,'transcripts/transcript.txt', multiproc = True)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)