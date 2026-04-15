Write-Output "Starting setup..."

if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
   Write-Output "Error: uv is not installed."
   Write-Output "Install uv first: https://docs.astral.sh/uv/getting-started/installation/"
   exit 1
}

Write-Output "Syncing uv projects..."
Get-ChildItem -Directory | ForEach-Object {
   if (Test-Path "$($_.FullName)\pyproject.toml") {
      Write-Output "Running uv sync in $($_.FullName)..."
      Push-Location $_.FullName
      uv sync
      Pop-Location
   }
}
Write-Output "uv projects synced."

Write-Output "Setup complete."
