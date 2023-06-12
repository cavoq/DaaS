# DaaS (Denial as a Service)

DaaS is an API that povides methods for denial of service attacks.

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

## Setup

You need to add API keys at the admin panel:
  
![image](https://github.com/cavoq/DaaS/assets/61215846/801315b9-aa15-4cf3-82ad-ebdb799c4392)

  
## Usage

See *make help*

![Screenshot from 2023-04-16 17-05-53](https://user-images.githubusercontent.com/61215846/232322016-6c2293a7-2132-40bb-931c-494dde30f0b3.png)


## Info

To see the API calls you can go to
```
http://<HOST>:<PORT>/docs
```

![Screenshot from 2023-04-16 17-04-46](https://user-images.githubusercontent.com/61215846/232322032-b34a7bee-c4e9-4fe2-abbe-74a3243e0469.png)

