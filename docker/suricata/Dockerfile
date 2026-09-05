FROM jasonish/suricata:latest

# Copy custom detection rules to the standard Suricata directory
COPY custom.rules /var/lib/suricata/rules/custom.rules

# Enable local rules in configuration
RUN echo "rule-files:" >> /etc/suricata/suricata.yaml && \
    echo "  - /var/lib/suricata/rules/custom.rules" >> /etc/suricata/suricata.yaml