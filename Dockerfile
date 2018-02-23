# Install base image
FROM resin/raspberrypi3-debian:latest

# Enable systemd
ENV INITSYSTEM on

# Add user credentials
RUN useradd -m "gooee" && \
    echo "root:smartsimple" | chpasswd && \
    echo "gooee:smartsimple" | chpasswd && \
    echo "gooee ALL=(ALL:ALL) ALL" >> /etc/sudoers

# Install base OS tools and dependencies
RUN apt-get update && apt-get -y install \
    build-essential \
    net-tools \
    openssh-server \
    rpi-update \
    vim \
    wget \
    python-dev \
    python-pip

# Install app tools and dependencies
RUN pip install -U \
    flask \
    unicornhat

# Setup app environment
COPY src /app
RUN chmod 744 /app/start.sh

# Start app
CMD ["bash", "/app/start.sh"]