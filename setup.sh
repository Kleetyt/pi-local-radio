#!/bin/bash

# Update the system
sudo apt update && sudo apt upgrade -y

# Install Python3 and pip
sudo apt install -y python3 python3-pip

# Install Flask
pip3 install Flask

# Create music folder if it doesn't exist
mkdir -p "$(dirname "$0")/music"

echo "Setup complete. You can start the server with: python3 app.py"
