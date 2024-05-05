# Structure from Motion Image Matcher

This repository contains a Python script that utilizes Structure from Motion (SfM) techniques to identify and select images nearest to given 3D points.

## Overview

The Structure from Motion (SfM) Image Matcher is a tool designed to streamline the process of selecting images that are the closest match to specified 3D points. By leveraging SfM algorithms, the script can analyze a collection of images and their corresponding camera positions to determine the proximity of each image to the provided 3D points.

![](`r https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=img#R7VdNb%2BIwEP01HJEICRCuUPohFRUtVVfamxsPiSUnjhyHAL9%2Bx8QmCaGFrsqKQ0%2FJPI%2Ft8XszE6fjTuPNgyRpNBcUeKffo5uOe9fp9x3P9fChkW2JjAYGCCWjxqkClmwHBuwZNGcUsoajEoIrljbBQCQJBKqBESlF0XRbCd7cNSUhtIBlQHgb%2Fc2oikrU748q%2FBFYGNmdneG4HImJdTYnySJCRVGD3FnHnUohVPkWb6bANXmWl3Le%2FQejh8AkJOqSCXzhv00f5y%2F%2BQA4pPN39gj%2BDrlllTXhuDry8n3efYjxWd05UEIE00autpSQrWMxJgtYkU0QqIxpu704iIdlOJIpwRDQQRIzTZ7IVuQ5SSQBr1HxfEcZRB0EJGduR9%2F1e%2B%2FnagSUgX7cpmBUQXiFs9nWQyUkKksWgQC5TErAkNLPbHNkDg1SwqUGGswcQuIzcoosd7RlBbQJbPYsqHYY2W6NaKvgGIyYDw8PSlUj4YnT6gmb9lmZvWCOipVMRMQWaD20XWJ6acxVzw3Sbm08z5GLCvF6DrxN0Ob0TdHnXosttp%2FhqfitkOeMbY8trsdWiCih2SGMCfxfFrAImewAH6o2gTqQUeUKBGivI5Xpv6GLNRC4DWJyuZGw0IagPButtaKiDSGjN%2Bpp2ZRTny68M6HzeabY%2BzQQJnCi2bn5vvl3X0Y%2BuZ3R1L9TV%2F25dzdSFYHiOWhttdobR4KjkDa3lrKPsOITx7wnjtxJmSmKQRFMuMryS3UgHdW%2FtezP%2BqbQzleZfWGn2VnX1Uht5zVI7zo0rl5o9Zy1l9jdwzSVw%2FKthIrmVcvP%2B34UFzervqOS6%2Bsd0Z38B`)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/Jonah-gr/SfM-Image-Matcher.git
```

2. Install the requirements:
```bash
pip install -r requirements.txt
```

## How to use

1. Set up the [config file](src/config.py):
Place a video of the object where you like it and change the perspective parameters.
NOTE: PyCOLMAP does not support cuda. To use your GPU anyway, install the right version [here](https://colmap.github.io/install.html). Then copy all the files inside this repository.

2. Run the script:

```bash
python -m src.main
```

Alternatively, use this [notebook](notebook/example.ipynb) and set up all the parameters there.



