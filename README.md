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

<img src="use_cases.png" width="400" height="200" alt="Use Cases diagram">

## Class Diagrams

![class diagrams](class_diagrams.png)

## Installation

Please see the [INSTALL](docs/INSTALL.md) guide for instructions.

## Usage

```python
# from pdfrw import PdfReader, PdfWriter
from previsedx_esopredict_pdf_file_utils import EsopredictPDFWriter as Writer
from previsedx_esopredict_pdf_file_utils import constants
import yaml
import os

config_file = constants.DEFAULT_CONFIG_FILE

# Load configuration file into dictionary.
config = yaml.safe_load(open(config_file))

outdir = os.path.join(
    constants.DEFAULT_OUTDIR_BASE,
    os.path.basename(__file__),
    constants.DEFAULT_TIMESTAMP,
)

# Create the output directory if it does not exist
os.makedirs(outdir, exist_ok=True)

# Output path for the populated PDF
outfile = os.path.join(outdir, "populated_output.pdf")

writer = Writer(
    config=config,
    config_file=config_file,
    outdir=outdir,
    outfile=outfile,
    verbose=True,
)

lookup = {
    "patient_name": "John Doe",
    "date_of_birth": "2024-01-02",
    "provider_name": "Dr. Jack Tripper",
    "gender": "Male",
    "medical_record_id": "12345",
    "previse_lab_id": "11112",
    "specimen_id": "7890",
    "collection_date": "2024-01-02",
    "date_received": "2024-02-02",
    "date_reported": "2024-03-02",
    "clinic": "Johns Hopkins Medical Center",
    "address": "123 Main St",
    "city_state_zip": "Baltmore, MD 12345",
    "treating_provider": "Dr. Smith",
    "barretts_diagnosis": "Something, Yes",
    "segment_length": "1.2",
    "risk_level": "High",
    "range_score": "8",
    "five_year_probability_of_progression": "14%",
    "notes": "Some notes from provider",
}

writer.write_file(**lookup)
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
