# Snake Game on AWS

This project is a Snake game created using Python (Pygbag) that is hosted on AWS. The game allows users to play, track their high scores, and compete to break their previous best. The game is hosted on Amazon Web Services (AWS) using Amazon S3 for storing the APK and other files, and AWS Amplify for hosting the game.

![SnakeRun - Google Chrome 2024-11-11 10-24-02](https://github.com/user-attachments/assets/1f7dd37c-1afe-4d11-8287-4839423c0c0a)

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Hosting Setup](#hosting-setup)
- [How to Play](#how-to-play)
- [How to Build and Run Locally](#how-to-build-and-run-locally)
---

## Project Overview

This is a browser-compatible Snake game created using Python and the **Pygbag** library, which allows us to build Python-based games that can run in a browser. The game is designed to be fun and challenging, where the player competes to achieve the highest score possible. The game is hosted on AWS, with the APK file and related assets stored in Amazon S3. AWS Amplify is used for deploying the game to the web.

---

## Features

- **High Score Tracking**: The game saves and displays the highest score, allowing players to compete against their own records.
- **Challenge Mode**: Players can attempt to break their high score through continuous gameplay.
- **AWS Hosting**: The APK file and game assets are uploaded to Amazon S3 and hosted via AWS Amplify for fast and reliable access.
- **Python Browser Compatibility**: The game is made browser-compatible using the Pygbag library, as traditional Python games (like those built with Pygame) are not supported by AWS Amplify.

---

## Technologies Used

- **Python**: The primary language used to develop the Snake game.
- **Pygbag**: A Python library that allows Python code to run in the browser, making it suitable for deployment on AWS Amplify.
- **AWS S3**: Used to store the APK file and game assets (such as images and sounds).
- **AWS Amplify**: Used for hosting the game and providing a web link for users to access it.
- **HTML5**: The game is packaged in an HTML format, which is then hosted on AWS Amplify.

---

## Hosting Setup

1. **Amazon S3**: 
   - The game APK file and associated resources (images, sounds, etc.) are uploaded to an S3 bucket.
   - Ensure that the S3 bucket is configured for public access to allow users to download the APK.

2. **AWS Amplify**:
   - AWS Amplify is used to host the game on the web.
   - Amplify is connected to the S3 bucket where the APK and game files are stored.
   - The URL provided by AWS Amplify allows users to access the hosted game via their browser.

---

## How to Play

1. Visit the [AWS Amplify Hosted Link](#link-to-your-game) in your browser.
2. Play the game using arrow keys to control the snake and try to eat the food.
3. Each time the snake eats food, it grows longer and the score increases.
4. The goal is to reach the highest possible score. Once you achieve a high score, it will be saved to track your progress.
5. Challenge yourself to break your previous high score!

---

## How to Build and Run Locally

### Prerequisites:
- Python 3.x
- `pygbag` library installed

### Steps to Run Locally:
1. Clone the repository or download the files to your local machine.
2. Install the required libraries by running:
   ```
   pip install pygbag
   ```
   ```
   pygbag main.py
   ```
