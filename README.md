# Real Time Stock Streaming Dashboard

## Project Overview

This data dashboard project is a simulated real-time stock trading dashboard built using **Python**, **Kafka**, **Streamlit**, and **Docker**. It mimics a live trading environment where fake buy/sell orders are generated or submitted manually, and the stock price reacts accordingly. This project demonstrates real-time data streaming using Kafka and real-time plotting with Streamlit.

Whether you're learning Kafka, Docker, or just want to simulate stock movements for fun or demo purposes—this app offers a clean and interactive experience.

## Dashboard Overview

- Displays data that updates in real time (every 0.5 seconds)
- Shows current stock price and timestamp
- Includes manual **Buy** and **Sell** buttons for user interaction
- Interactive Plotly chart visualizing price over time

## Demo Video (youtube)

<div align="center">
  <a href="https://www.youtube.com/watch?v=za2ShawmdGQ" target="_blank">
    <img src="https://img.youtube.com/vi/za2ShawmdGQ/0.jpg" width="480" alt="Demo Video">
  </a>
</div>

## Architecture

### Producer (Random Orders) → Kafka → Consumer (Price Update) → Shared JSON → Streamlit Dashboard

- Kafka acts as the streaming backbone.
- A producer generates simulated buy/sell orders.
- A consumer listens for these events and updates a shared JSON file with new prices.
- The Streamlit dashboard reads from this shared file to visualize live trading data.

## Repository Contents

- `producer/`: Generates and sends simulated orders to Kafka.
- `consumer/`: Consumes Kafka events and updates the shared price file.
- `shared/`: Stores `price_data.json`, the live price file.
- `streamlit_dashboard/`: Streamlit dashboard that reads price data and allows user trades.
- `docker-compose.yml`: Spins up Kafka, Zookeeper, Producer, Consumer, and Streamlit.

## Getting Started

### Step 1: Build and Run All Services

```bash
docker-compose up --build
```

### Step 2: Access the Dashboard
Open your browser and go to:
```bash
http://localhost:8501/
```