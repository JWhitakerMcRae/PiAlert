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

# Allow ssh (and scp) as root
#RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/g' /etc/ssh/sshd_config

# Install app tools and dependencies
RUN pip install -U \
    flask \
    unicornhat

# Setup app environment
COPY src /app
COPY start.sh /usr/local/bin

# Start app
CMD ["bash", "start.sh"]