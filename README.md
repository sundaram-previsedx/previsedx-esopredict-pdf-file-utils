# previsedx-esopredict-pdf-file-utils

Collection of Python modules for processing Esopredict PDF final report files.

- [previsedx-esopredict-pdf-file-utils](#previsedx-esopredict-pdf-file-utils)
  - [Improvements](#improvements)
  - [Use Cases](#use-cases)
  - [Class Diagrams](#class-diagrams)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [To-Do/Coming Next](#to-docoming-next)
  - [CHANGELOG](#changelog)
  - [License](#license)


## Improvements

Please see the [TODO](docs/TODO.md) for a list of upcoming improvements.

## Use Cases

<img src="use_cases.png" width="400" height="400" alt="Use Cases diagram">

## Class Diagrams

![class diagrams](class_diagrams.png)

## Installation

Please see the [INSTALL](docs/INSTALL.md) guide for instructions.

## Usage

```python
from previsedx_esopredict_pdf_file_utils import constants
from previsedx_esopredict_pdf_file_utils import EsopredictPDFWriter as Writer

config_file = "conf/config.yaml"
if not os.path.exists(config_file):
  config_file = constants.DEFAULT_CONFIG_FILE
config = yaml.safe_load(Path(config_file).read_text())

writer = Writer(
    config=config,
    config_file=config_file,
    logfile=logfile,
    outdir=outdir,
    outfile=outfile,
    verbose=verbose,
)

writer.write_file()
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## To-Do/Coming Next

Please view the listing of planned improvements [here](docs/TODO.md).

## CHANGELOG

Please view the CHANGELOG [here](docs/CHANGELOG.md).

## License

[GNU AFFERO GENERAL PUBLIC LICENSE](docs/LICENSE)
