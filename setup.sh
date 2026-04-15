#!/usr/bin/env bash

# This script will run automatically when executed
# set it to execution

set -e

echo "Starting setup..."

if ! command -v uv >/dev/null 2>&1; then
   echo "Error: uv is not installed."
   echo "Install uv first: https://docs.astral.sh/uv/getting-started/installation/"
   exit 1
fi

echo "Syncing uv projects..."
for dir in */; do
   if [ -f "$dir/pyproject.toml" ]; then
      echo "Running uv sync in $dir..."
      (
         cd "$dir"
         uv sync
      )
   fi
done
echo "uv projects synced."

echo "Setup complete."