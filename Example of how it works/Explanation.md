# Facial Recognition Process Documentation

## Overview

This documentation outlines the process flow for the facial recognition system that detects a user's face, identifies them, and generates a personalized HTML page with their details.

## Process Flow

1. **Face Detection:**
   ![Analyzing Face](1_Analyzing_Face.png)
   - The system starts by capturing a live feed from the camera.
   - It then analyzes the incoming frames to detect any faces present using a face detection algorithm.

2. **Face Analysis:**
   ![After Analyzing Face](2_After_Analyzing_Face.png)
   - Once a face is detected, the system begins the analysis.
   - User must enter [S] to send a photo of your face to the machine_learning.py so it can determine who the face belongs too

3. **Terminal Output:**
   ![Example Terminal Output](3_Example_Terminal_Output.png)
   - The identified face is matched against a database of known individuals.
   - A match percentage is calculated, and if the threshold is met, the identification is considered successful.

4. **Personalized HTML Page Generation:**
   ![ChatGPT API creating custom HTML page of individual](4_ChatGPT_API_creating_custom_HTML_page_of_individual.png)
   - Post-identification, the system leverages the OpenAI GPT-4 model to generate a custom HTML page.
   - This page includes the individual's information, such as gender, ethnicity, address, occupation, and educational details.
