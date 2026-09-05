FROM kalilinux/kali-rolling

# Prevent interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install essential penetration testing and network diagnostic tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    nmap \
    hydra \
    hping3 \
    curl \
    iputils-ping \
    iproute2 \
    net-tools \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set default working directory for attack scripts and logs
WORKDIR /attacks

CMD ["sleep", "infinity"]