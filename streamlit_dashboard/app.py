import streamlit as st
import pandas as pd
import json
import time
import os
from datetime import datetime
from kafka import KafkaProducer
import plotly.express as px

st.set_page_config(page_title="📈 HAHN Dashboard", layout="centered")
st.title("📈 Real-Time HAHN Stock Dashboard")

# Kafka producer setup
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

shared_path = "/shared/price_data.json"
placeholder = st.empty()

while True:
    try:
        if os.path.exists(shared_path):
            with open(shared_path, "r") as f:
                data = json.load(f)

            if data:
                df = pd.DataFrame(data)
                df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
                latest_price = df["price"].iloc[-1]
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                fig = px.line(
                    df,
                    x="timestamp",
                    y="price",
                    title="HAHN Stock Price Over Time",
                    labels={"timestamp": "Time", "price": "Price (USD)"}
                )
                fig.update_traces(mode="lines+markers")
                fig.update_layout(
                    xaxis=dict(showgrid=True),
                    yaxis=dict(showgrid=True),
                    margin=dict(l=40, r=40, t=60, b=40)
                )

                # ⏱️ LIVE UI UPDATES
                with placeholder.container():
                    st.plotly_chart(fig, use_container_width=True)

                    col1, col2 = st.columns(2)

                    with col1:
                        st.markdown("### ℹ️ Live Data")
                        st.markdown(
                            f"""
                            <div style='font-size: 22px;'>
                                🕒 <strong>Timestamp:</strong> {current_time}<br>
                                💰 <strong>Current Price:</strong> ${latest_price:.2f}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    with col2:
                        st.markdown("### ⚙️ Manual Trade Controls")
                        if st.button("📥 Buy HAHN", key="buy_button"):
                            order = {"action": "buy", "stock": "HAHN", "quantity": 5, "timestamp": time.time()}
                            producer.send('stock_orders', order)

                        if st.button("📤 Sell HAHN", key="sell_button"):
                            order = {"action": "sell", "stock": "HAHN", "quantity": 5, "timestamp": time.time()}
                            producer.send('stock_orders', order)

            else:
                st.warning("No price data yet. Waiting for producer...")
        else:
            st.error("price_data.json not found in /shared directory.")

    except Exception as e:
        st.warning(f"Error reading data: {e}")

    time.sleep(0.5)
