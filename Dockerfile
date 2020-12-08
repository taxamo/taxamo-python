FROM n42org/tox
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y libcurl4-openssl-dev libssl-dev build-essential libffi-dev python3-pip python3.8-dev python3.8-distutils python3.8-venv python3.9-dev
