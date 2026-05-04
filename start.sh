#!/bin/bash

echo "Installing FFmpeg..."
apt-get update && apt-get install -y ffmpeg

echo "Checking FFmpeg..."
ffmpeg -version

echo "Installing Python dependencies..."
pip3 install -r requirements.txt

echo "Starting app..."
python3 app.py#!/bin/bash

echo "Installing FFmpeg..."

apt-get update
apt-get install -y ffmpeg

echo "Checking FFmpeg..."
ffmpeg -version

echo "Installing Python dependencies..."
pip3 install -r requirements.txt

echo "Starting app..."
python3 app.py#!/bin/bash

echo "Installing FFmpeg..."
apt-get update && apt-get install -y ffmpeg

echo "Installing Python dependencies..."
pip3 install -r requirements.txt

echo "Starting app..."
python3 app.py
