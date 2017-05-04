#!/bin/ash

# Add required packages
cat <<'EOF'>> /etc/opkg/customfeeds.conf
src/gz jarvis_respeaker_base https://iopush.net/Jarvis/Respeaker/packages/base
src/gz jarvis_respeaker_packages https://iopush.net/Jarvis/Respeaker/packages/packages
EOF

# Disable signature verifications
# TODO : Generate package signature
# WARNING - Not safe
sed -i '/option check_signature 1/d' /etc/opkg.conf

# Update packages list and install bash
opkg update
opkg install bash git git-http sudo

git clone -b respeaker --single-branch https://github.com/oliv4945/jarvis.git

