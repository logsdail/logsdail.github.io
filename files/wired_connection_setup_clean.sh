#!/bin/sh

# This small script is designed to set up a wired connection with the TLS protocol and 802-1x
# network authentication. This is intended for Linux machines, and works without issues for
# Fedora 36.

# Use for script - Place this script in a folder with your ca-cert, client-cert and private-key.
# You will need to provide: Name of the ethernet network (ETHNAME) and PRIVATE_KEY_PASSWORD.

# wireless name obtained from identity of ethernet connection from network GUI.

mv OnboardCertificate.pkcs12 OnboardCertificate.p12
CURRENT_DIRECTORY=$PWD

# Input your variable names here. 
ETHNAME="eduroam"
PRIVATE_KEY_PASSWORD=

# Add the email address to the line 802-1x.indentity
nmcli c add type ethernet ifname $ETHNAME con-name 'Wired_Connection' \
      802-1x.eap tls \
      802-1x.identity USERNAME@cardiff.ac.uk  \
      802-1x.ca-cert $CURRENT_DIRECTORY/CardiffUniversityRootCA.crt \
      802-1x.client-cert $CURRENT_DIRECTORY/ClearPass_Onboard_Certificate_Authority.crt \
      802-1x.private-key $CURRENT_DIRECTORY/OnboardCertificate.p12 \
      802-1x.private-key-password $PRIVATE_KEY_PASSWORD


