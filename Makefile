NAME=denialofservice-api
PYTHON=python3
PORT=5000
MAIN=server
LOG_DIR=logs
VERSION=3.0.1
CURRENT_DIR=$(shell pwd)


help: ## Get help for Makefile
	@echo "\n#### $(NAME) v$(VERSION) ####\n"
	@echo "Available targets:\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@echo "\n"

install: ## Install requirements locally
	sudo pip3 install -r requirements.txt

install-dev: ## Install requirements locally for development
	sudo pip3 install -r requirements-dev.txt

test: ## Run tests
	sudo $(PYTHON) -m pytest tests/

docker-build: ## Build docker image
	docker build -t $(NAME) .

docker-run: ## Run api inside docker container
	docker run --network=host --env-file .env -p $(PORT):$(PORT) -v $(CURRENT_DIR)/$(LOG_DIR):/denialofserviceAPI/$(LOG_DIR) --name denialofservice-api $(NAME)

docker-sh: ## Shell into docker container
	docker run -it $(NAME) sh

docker-remove: ## Remove docker container
	docker rm -f $(NAME)
	
run: ## Run api on host machine
	sudo $(PYTHON) $(MAIN).py direct $(HOST) $(PORT)

clear-log: ## Clear log file
	@rm -f $(LOG_FILE)

.PHONY: help docker-build docker-run docker-sh run clear-log install install-dev test