<p align="center">
  <img width="300" src="https://image.tensorartassets.com/cdn-cgi/image/anim=true,f=avif,q=85/frontend/1711339876825.svg">
</p>

<div align="center">
    <a href="https://badge.fury.io/py/tensorart"><img src="https://d25lcipzij17d.cloudfront.net/badge.svg?id=py&r=r&ts=1683906897&type=6e&v=0.1&x2=0" alt="PyPI version" height="18"></a>
</div>


<div>
TensorART is a hybrid API for tensor.art. It is able to communicate with Tensor
using web-scraping.. It is
able to access most used or useful ai features, such as text2img, img2img , upscale, and a lot more.
</div>

> [!WARNING]
> This project is probably against TensorART TOS. Use at your own risks.

## Installation

- Install using `pip` (python `3.11` or higher required, recommended version): 
```shell
pip install --upgrade TensorART
```

- Or from this repo to get the latest fixes/features:
```shell
pip install --upgrade git+https://github.com/XZeipher/TensorAI.git
```

- Or, for python 3.10 and higher.
```shell
pip install --upgrade git+https://github.com/XZeipher/TensorAI.git@py-3.10
```

- Or, for even lower python versions, there is automatic branch with several features removed (might be unstable).
```shell
pip install --upgrade git+https://github.com/XZeipher/TensorAI.git@compat
```

## Quickstart

> [!NOTE]
> You can find the docs on this project [here](https://tensorapi.onrender.com/docs).

```python
from TensorART import TensorClient
import aiohttp,aiofiles

# Initialise a client
client = TensorClient()

# Create ai image
image_url = await client.create(model_id=1,prompt="blonde girl sitting in garden")

# save image binary data
async with aiohttp.ClientSession as session:
    async with session.get(image_url) as response:
        async with aiofiles.open('image.png','wb') as f:
            await f.write(await response.content)

# image will be saved as image.png

```

# Note
<strong>This repository is initiated and maintained by [XZeipher](https://github.com/XZeipher)
</strong>


## License

TensorART uses GPLv3. See the `LICENSE` file.

## Contributing

Feel free to contribute to this project by submitting
feature requests, issues, bugs, or whatever.
