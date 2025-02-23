Write-Output "Starting setup..."

if (Test-Path ".venv") {
   Write-Output "Directory .venv already exists."
   Write-Output "Skipping virtual environment installation."
}
else {
   Write-Output "Directory .venv does not exist."
   Write-Output "Installing virtual environment..."
   python -m venv .venv
   Write-Output "Virtual environment installed."
}

Write-Output "Starting the virtual environment..."
& .\.venv\Scripts\Activate.ps1
Write-Output "Virtual environment started."

Write-Output "Installing Python requirements..."
Get-ChildItem -Directory | ForEach-Object {
   if (Test-Path "$($_.FullName)\requirements.txt") {
      Write-Output "Installing requirements in $($_.FullName)..."
      pip install -r "$($_.FullName)\requirements.txt"
   }
}
Write-Output "Python requirements installed."

Write-Output "Setup complete."
