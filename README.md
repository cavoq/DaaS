# DaaS (Denial as a Service)

DaaS is an api that povides methods for denial of service attacks.

![license](https://img.shields.io/badge/license-MIT-brightgreen.svg)
![version](https://img.shields.io/badge/version-3.0.1-lightgrey.svg)

## Requirements
For this script to work, you need to have [Docker](https://www.docker.com/products/docker-desktop) installed

## Setup

See *.env* file

```
PORT=5000
DATABASE_URL=sqlite:///db/denialofservice.db
TEST_DATABASE_URL=sqlite:///db/denialofservice_test.db
MOCK=0
```

## Usage

See *make help*

![Screenshot from 2023-04-09 11-35-36](https://user-images.githubusercontent.com/61215846/230765647-14ebff7c-860a-482f-8e91-ba1607030546.png)


## Info

To see the API calls you can go to
```
http://<HOST>:<PORT>/docs
```
![image](https://user-images.githubusercontent.com/61215846/221359714-040caa53-5755-45d3-9e49-f9541fb47259.png)
