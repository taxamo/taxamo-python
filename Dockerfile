FROM n42org/tox
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y libcurl4-openssl-dev libssl-dev build-essential libffi-dev