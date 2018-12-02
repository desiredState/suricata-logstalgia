# Suricata Logstalgia

Streams Suricata EVE logs to Logstalgia Custom Log Format.

### Usage 

```bash
docker run --rm \
    --mount type=bind,src=/usr/local/var/log/suricata/eve.json,dst=/eve.json,readonly \
    desiredstate/suricata-logstalgia:latest | tee /dev/tty | \
    logstalgia --sync -x -g "Suricata IDS,CODE=.*?,100"
```
