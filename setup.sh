#!/usr/bin/env bash

# This script will run automatically when executed
# set it to execution

echo "Starting setup..."

if [ -d ".venv" ]; then
   echo "Directory .venv already exists."
   echo "Skipping virtual environment installation."
else
   echo "Directory .venv does not exist."
   echo "Installing virtual environment..."
   python3 -m venv .venv
   echo "Virtual environment installed."
fi

echo "Starting the virtual environment..."
source .venv/bin/activate
echo "Virtual environment started."

echo "Installing Python requirements..."
for dir in */; do
   if [ -f "$dir/requirements.txt" ]; then
      echo "Installing requirements in $dir..."
      pip install -r "$dir/requirements.txt"
   fi
done
echo "Python requirements installed."

echo "Setup complete."