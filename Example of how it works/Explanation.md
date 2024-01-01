# Facial Recognition Process Documentation

## Overview

This documentation outlines the process flow for the facial recognition system that detects a user's face, identifies them, and generates a personalized HTML page with their details.

## Process Flow

1. **Analyzing Face:**
   - The system starts by capturing a live feed from the camera.
   - It then analyzes the incoming frames to detect any faces present using a face detection algorithm.
   - User must enter [S] to send a photo of your face to the machine_learning.py so it can determine who the face belongs to

2. **After Analyzing Face:**
   - After analysis, machine_learning.py will return who the face belongs to

3. **Terminal Output:**
   - The identified face is matched against a database of known individuals.
   - A match percentage is calculated, and if the threshold is met, the identification is considered successful.

4. **Personalized HTML Page Generation created by ChatGPT:**
   - Post-identification, the system leverages the OpenAI GPT-4 model to generate a custom HTML page.
   - This page includes the individual's information, such as gender, ethnicity, address, occupation, and educational details.
