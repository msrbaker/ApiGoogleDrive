SHELL = /bin/bash

.PHONY: secrets all shell-nginx shell-app log-nginx log-app backup-logs collectstatic deploy upgrade

all:
	@echo "Available commands:"
	@echo -e "\tshell-{nginx,app}: execute a shell inside the container\n\tlog-{nginx,app}: show the container logs\n\tcollectstatic: execute Django collectstatic in the app container\n\tsecrets: create and populate .env file\n\tbackup-logs: backup logs\n\tdeploy: initial deployment\n\tupgrade: update source code and launch app"

shell-nginx:
	docker-compose exec nginx ash

shell-app:
	docker-compose exec app ash

log-nginx:
	docker-compose logs nginx

log-app:
	docker-compose logs app

collectstatic:
	docker-compose exec app /bin/ash -c "python manage.py collectstatic --noinput"

backup-logs:
	@echo "Backing up logs..."
	@if [ ! -d "backups" ]; then mkdir backups; fi;
	@echo "Backing up logs..."
	docker-compose logs --no-color app | gzip -v -9 -c > backups/app-logs-$(shell date +"%Y%m%d_%H%M%S").log.gz
	docker-compose logs --no-color nginx | gzip -v -9 -c > backups/nginx-logs-$(shell date +"%Y%m%d_%H%M%S").log.gz

secrets:
	@if [ -f ".env" ]; \
	then \
		echo "file exists! bailing out"; \
		exit 1; \
	fi;
	@printf "%s" "APP_SECRET_KEY=" >> .env
	@LC_CTYPE=C tr -dc 'a-zA-Z0-9_+-.' < /dev/urandom | dd bs=64 count=1 iflag=fullblock status=none 2> /dev/null >> .env
	@echo >> .env
	@grep -v APP_SECRET_KEY env >> .env
	@chmod 0440 .env

deploy: secrets
	@read -sr -n 1 -p "Complete .env config and press a key to continue (check the README for more info)" && echo
	docker-compose config
	@echo "Copying source code..."
	@[ -d "./app" ] || rm -rf ./app;
	@cp -pr ../app ./app
	@echo "Creating directories..."
	mkdir backups 2>/dev/null || echo "Backups dir exists"
	@echo "Building images..."
	docker-compose build
	docker-compose up -d
	@sleep 1
	@echo "Initializing app..."
	docker-compose exec app /bin/ash -c "python manage.py collectstatic --noinput"
	docker-compose exec app /bin/ash -c "python manage.py migrate --noinput"
	@echo "All done!"

upgrade: backup-logs
	@echo "Copying source code..."
	@[ -d "./app" ] || rm -rf ./app;
	@cp -pr ../app ./app
	@echo "Rebuilding app..."
	docker-compose build app
	@echo "Stopping containers..."
	docker-compose stop
	docker-compose rm -sf app
	@echo "Starting containers..."
	docker-compose up -d
	@echo "Reinitializing app: compiling translations and collecting static files..."
	#docker-compose exec app /bin/ash -c "python manage.py compilemessages"
	#docker-compose exec app /bin/ash -c "python manage.py collectstatic --noinput"
	@echo "Listing migrations..."
	docker-compose exec app /bin/ash -c "python manage.py showmigrations --list"
	@echo "You might want to execute migrations..."
	#docker-compose exec app /bin/ash -c "python manage.py migrate --noinput"
	@echo "All done!"
