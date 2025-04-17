build:
	docker build -t prom-flask -f Dockerfile .
rerun:
	docker stop prom
	docker rm prom
	docker run -d --name prom -p "8080:8080" prom-flask:latest
run:
	docker run -d --name prom -p "8080:8080" prom-flask:latest
stop:
	docker stop prom