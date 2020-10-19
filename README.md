![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
[![GitHub stars](https://img.shields.io/github/stars/OnePoint-Team/DAC-autoreg.svg)](https://github.com/OnePoint-Team/DAC-autoreg/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/OnePoint-Team/DAC-autoreg.svg)](https://github.com/OnePoint-Team/DAC-autoreg/network)
[![GitHub issues](https://img.shields.io/github/issues-raw/OnePoint-Team/DAC-autoreg)](https://github.com/OnePoint-Team/DAC-autoreg/issues)
<!-- [![Downloads](https://pepy.tech/badge/dac-autoreg)](https://pepy.tech/project/dac_autoreg) -->

### About ###

This module is used to register `endpoints` and `service names` to `DAC` [Dyncamic Access Control] service.

`DAC` [Dyncamic Access Control] service is used to control accesses between `microservices` and `users`

Visit https://github.com/OnePoint-Team/DAC for more information about `DAC` service


###  🔨  Installation ###
```sh
 $ sudo pip3 install dac_autoreg
```

### 🕹 Python Module
```python
from fastapi import FastAPI
from core.factories import settings
from core.extensions import log

from dac_autoreg.modules import Autoreg

app = FastAPI()

@app.on_event("startup")
async def startup():
    await Autoreg(app=app, log=log, settings=settings).autoreg()
```

## Supported OS
Linux, MacOS

## 🌱 Contributing
Feel free to open issue and send pull request.

### Python >= 3.6