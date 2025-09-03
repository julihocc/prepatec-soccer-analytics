#!/usr/bin/env python3
"""
🚀 QTI GENERATOR - txttoqti v0.3.0 Wrapper
Minimal wrapper that uses txttoqti-edu CLI for backward compatibility.

This script provides the same interface as before but uses the official
txttoqti v0.3.0 educational module instead of local implementation.

Features:
- Same command-line interface for backward compatibility
- Uses txttoqti v0.3.0 educational auto-detection system
- Zero maintenance - all functionality handled by txttoqti library
- Enhanced error handling and validation

Usage:
    python generar_qti.py [--status] [--force] [--interactive] [--help]
    
Arguments:
    --status        Show current status without conversion
    --force         Force regeneration even if no changes detected
    --interactive   Enable interactive mode for format validation
    --help          Show help message
"""

import subprocess
import sys
import os
from pathlib import Path


def find_txttoqti_edu():
    """Find txttoqti-edu command in virtual environment or system PATH."""
    # Try virtual environment first
    script_dir = Path(__file__).parent
    
    # Walk up to find repository root with .venv
    current_dir = script_dir
    for _ in range(10):  # Search up to 10 levels up
        venv_bin = current_dir / ".venv" / "bin" / "txttoqti-edu"
        if venv_bin.exists():
            return str(venv_bin)
        current_dir = current_dir.parent
        if current_dir == current_dir.parent:  # Reached filesystem root
            break
    
    # Try system PATH
    try:
        result = subprocess.run(['which', 'txttoqti-edu'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
    except:
        pass
    
    return None


def show_help():
    """Show help message."""
    print(__doc__)


def main():
    """Main function - wrapper for txttoqti-edu."""
    
    # Handle help locally for better messaging
    if '--help' in sys.argv or '-h' in sys.argv:
        show_help()
        return
    
    # Find txttoqti-edu command
    txttoqti_edu_path = find_txttoqti_edu()
    
    if not txttoqti_edu_path:
        print("❌ Error: txttoqti-edu no encontrado")
        print("   Instala txttoqti v0.3.0+: pip install git+https://github.com/julihocc/txttoqti.git@v0.3.0")
        print("   O activa el entorno virtual: source .venv/bin/activate")
        sys.exit(1)
    
    # Pass all arguments to txttoqti-edu
    cmd_args = [txttoqti_edu_path] + sys.argv[1:]
    
    try:
        result = subprocess.run(cmd_args)
        sys.exit(result.returncode)
    except Exception as e:
        print(f"❌ Error ejecutando txttoqti-edu: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()