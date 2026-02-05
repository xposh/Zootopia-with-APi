# Zootopia - Animal Data Web Generator

A Python tool that fetches live animal data from the **Ninja API** and generates a structured HTML website.

## Installation

1. Install dependencies:
   `pip install -r requirements.txt`

2. Create a `.env` file in the root folder and add your API key:
   `API_KEY='your_api_key_here'`

## Usage

Run the generator:
`python animals_web_generator.py`

Enter an animal name when prompted. The output will be saved in `animals.html`.

## Features
* Live API integration with API-Ninjas.
* Secure API key management via `.env`.
* Modular architecture.