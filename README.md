# KwcyDOSApI

KwcyDOSApI is an Api that povides methods for Denial-of-service attacks

## Requirements
For this script to work, you need to have Docker installed

## Build
**1. Clone the repository**
```
git clone https://github.com/Dav3o/KwcyDOSApI.git
```
Go into the cloned repository
```
cd KwcyDOSApI
```
Build the docker image
```
Docker build .
```
## Usage

You can run the container with following commands
```
Docker run -e HOST=<HOST> -e PORT=<PORT> -p <HOST_PORT>:<CONTAINER_PORT> IMAGE_NAME
```
If you want to specify the host and the port in the *.env* file
```
Docker run --env-file .env -p -p <HOST_PORT>:<CONTAINER_PORT> IMAGE_NAME
```
*Note:* if you don't specify anything the default host will be set to 0.0.0.0:5000

## Info

To see the API calls you can go to
```
http://<HOST>:<PORT>/docs
```
![Bildschirmfoto vom 2022-03-02 00-28-15](https://user-images.githubusercontent.com/61215846/156266224-636846b0-6976-4503-87db-c87cd01b46df.png)
