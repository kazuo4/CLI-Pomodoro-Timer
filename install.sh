#!/bin/bash

# 1. Get the absolute path of the folder where this install script is running
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE}")" && pwd)"

# 2. Make sure the helper script is set to executable
chmod +x "$PROJECT_DIR/mytimer"

# 3. Check if the worktimer alias already exists in their Zsh profile
if grep -q "alias worktimer=" ~/.zshrc; then
    echo "🔄 Updating existing worktimer alias in ~/.zshrc..."
    # Safely removes the old alias line to prevent duplicate stacking
    sed -i '' '/alias worktimer=/d' ~/.zshrc
fi

# 4. Append the clean, calculated dynamic alias straight to the bottom of their profile
echo "alias worktimer=\"$PROJECT_DIR/mytimer\"" >> ~/.zshrc

echo "✅ Success! 'worktimer' alias configured automatically."
echo "👉 Run 'source ~/.zshrc' or open a new window to start using it from anywhere!"
