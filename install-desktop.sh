#!/bin/sh
# Add Coding Trainer to the current user's application menu (no root needed).
# Remove it again with: rm ~/.local/share/applications/coding-trainer.desktop
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
APPS="$HOME/.local/share/applications"
mkdir -p "$APPS"
cat > "$APPS/coding-trainer.desktop" <<EOF
[Desktop Entry]
Type=Application
Name=Coding Trainer
Comment=Daily coding problems in C, C++, Python and Rust
Exec=/usr/bin/python3 $DIR/src/gui.py
Icon=$DIR/assets/coding-trainer.svg
Terminal=false
Categories=Development;
StartupWMClass=coding-trainer
EOF
desktop-file-validate "$APPS/coding-trainer.desktop"
update-desktop-database "$APPS"
echo "Installed $APPS/coding-trainer.desktop"
