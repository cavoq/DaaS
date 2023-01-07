DOCKER_NAME=denialofservice-api
PYTHON=python3
HOST=0.0.0.0
PORT=5000
MAIN=server
LOG_FILE=info.log


help: ## Get help for Makefile
	@echo "\n#### DenialofServiceAPI v1.0 ####\n"
	@echo "Available targets:\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@echo "\n"

install: ## Install requirements locally
	sudo pip3 install -r requirements.txt
	
docker-build: ## Build docker image
	docker build -t $(DOCKER_NAME) .

docker-run: ## Run api inside docker container
	docker run --env-file .env -p 5000:5000 --name dos-api $(DOCKER_NAME)

docker-sh: ## Shell into docker container
	docker run -it $(DOCKER_NAME) sh

run: ## Run api on host machine
	$(PYTHON) $(MAIN).py direct $(HOST) $(PORT)

clear-log: ## Clear log file
	@rm -f $(LOG_FILE)

.PHONY: help docker-build docker-run docker-sh run clear-log