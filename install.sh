#!/bin/bash

# Define where the application will live permanently on the user's Mac
TARGET_DIR="$HOME/.cli-pomodoro-timer"

echo "🍅 Starting CLI Pomodoro Timer Installation..."

# 1. Handle downloading or local execution dynamically
if [ -d ".git" ]; then
    # If they already downloaded the folder locally, use it
    PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    echo "📦 Copying files to installation directory..."
    mkdir -p "$TARGET_DIR"
    cp -R "$PROJECT_DIR/"* "$TARGET_DIR/"
else
    # If they ran the curl command, clone the code directly from GitHub
    echo "🌐 Cloning repository from GitHub..."
    rm -rf "$TARGET_DIR"
    git clone --quiet https://github.com/kazuo4/CLI-Pomodoro-Timer.git "$TARGET_DIR"
fi

# 2. Automatically build the Python virtual environment sandbox silently
echo "⚙️  Setting up isolated Python environment..."
python3 -m venv "$TARGET_DIR/myenv"
"$TARGET_DIR/myenv/bin/pip" install --quiet rumps playsound3

# 3. Secure executable rights on the launcher script
chmod +x "$TARGET_DIR/mytimer"

# 4. Clean out any old/broken worktimer configurations from their profile
if grep -q "worktimer()" ~/.zshrc || grep -q "alias worktimer=" ~/.zshrc; then
    sed -i '' '/alias worktimer=/d' ~/.zshrc
    sed -i '' '/worktimer()/,/}/d' ~/.zshrc
fi

# 5. Append the permanent Zsh function to the bottom of their profile
cat << FUNC >> ~/.zshrc

worktimer() {
    "$TARGET_DIR/mytimer" "\$1"
}
FUNC

echo "✅ Success! Installation complete."
echo "👉 Open a new terminal window or run 'source ~/.zshrc' to start using 'worktimer'!"
