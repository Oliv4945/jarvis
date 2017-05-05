#!/bin/ash

# Add required packages
cat <<'EOF'>> /etc/opkg/customfeeds.conf
src/gz jarvis_respeaker_base https://iopush.net/Jarvis/Respeaker/packages/base
src/gz jarvis_respeaker_packages https://iopush.net/Jarvis/Respeaker/packages/packages
EOF

# Add opkg key
cat <<'EOF'>> /tmp/b51f350377af8a5a
untrusted comment: public key b51f350377af8a5a
RWS1HzUDd6+KWig9kocRWRS+aBZZWc1L4cjeSWoQyt2vMW0+p1Vonxa+
EOF
opkg-key add /tmp/b51f350377af8a5a

# Update packages list and install bash
opkg update
opkg install bash git git-http sudo

git clone -b respeaker --single-branch https://github.com/oliv4945/jarvis.git

