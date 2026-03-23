#!/bin/bash
# Build script for WARP Indicator

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_NAME="warp-indicator"
PROJECT_VERSION="1.0.0"

echo "Building $PROJECT_NAME v$PROJECT_VERSION..."

# Install dependencies
echo "Installing dependencies..."
sudo apt-get update
sudo apt-get install -y \
    python3 \
    python3-gi \
    gir1.2-appindicator3-0.1 \
    gir1.2-gtk-3.0 \
    dh-python \
    debhelper

# Create build directory
BUILD_DIR="${SCRIPT_DIR}/build"
rm -rf "$BUILD_DIR"
mkdir -p "$BUILD_DIR"

# Copy files to build directory
cp -r "$SCRIPT_DIR" "$BUILD_DIR/$PROJECT_NAME-$PROJECT_VERSION"

# Build the Debian package
cd "$BUILD_DIR/$PROJECT_NAME-$PROJECT_VERSION"
dpkg-buildpackage -us -uc

echo "Build complete! Check $BUILD_DIR for .deb file"
