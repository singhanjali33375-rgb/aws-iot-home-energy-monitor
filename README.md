# aws-iot-home-energy-monitor
A cloud-based home energy monitoring system built using AWS IoT Core, AWS Lambda, Amazon CloudWatch, and Amazon S3 that tracks real-time energy consumption and provides insights through a web dashboard.
# ⚡ Home Energy Monitoring System using AWS IoT

A cloud-based home energy monitoring system that tracks real-time electricity
consumption using AWS IoT Core, processes data using AWS Lambda, stores metrics
in Amazon CloudWatch, and visualizes insights through a web dashboard hosted
on Amazon S3.

---

## 🚀 Project Overview

This project enables users to monitor their home energy usage in real time.
Energy data is sent from IoT devices to AWS IoT Core, processed using serverless
functions, and stored as metrics in CloudWatch. A web dashboard hosted on Amazon
S3 allows users to visualize usage patterns and gain insights to optimize energy
consumption.

---

## 🛠️ Technologies Used

- AWS IoT Core
- AWS Lambda (Python)
- Amazon CloudWatch
- Amazon S3 (Static Website Hosting)
- AWS IAM
- JSON / MQTT

---

## ✨ Features

- Real-time energy consumption tracking
- Secure data ingestion using AWS IoT Core
- Serverless data processing with AWS Lambda
- Energy usage metrics stored in CloudWatch
- Web dashboard for visualization
- Scalable and cost-efficient architecture

---

## 🏗️ Architecture

IoT Device → AWS IoT Core → AWS Lambda → Amazon CloudWatch → S3 Web Dashboard

(Architecture diagram included in the repository)

---

## 🔄 How It Works

1. Energy sensor sends data to AWS IoT Core using MQTT
2. AWS IoT Rule triggers a Lambda function
3. Lambda processes energy data and publishes metrics to CloudWatch
4. CloudWatch stores and aggregates energy usage data
5. Dashboard hosted on S3 visualizes energy consumption trends

---

## 📥 Sample IoT Message

```json
{
  "deviceId": "energy-sensor-001",
  "timestamp": "2026-02-04T10:30:00Z",
  "powerUsage": 1.8
}
📊 Dashboard Features
Real-time energy usage
Daily and monthly consumption trends
Visualization using charts
Simple and responsive UI
⚙️ Setup Instructions
Create an AWS IoT Thing and generate certificates
Configure IoT Rule to trigger AWS Lambda
Deploy Lambda function to process energy data
Create CloudWatch metrics for energy usage
Host the web dashboard on Amazon S3
🚧 Future Enhancements
Mobile application support
Energy consumption alerts
Machine learning based predictions
Integration with smart home devices
Historical data storage using DynamoDB or Timestream
📄 License
This project is open-source and intended for educational purposes.
“This project collects energy consumption data from IoT devices using AWS IoT Core.
The data is processed using AWS Lambda and stored as metrics in Amazon CloudWatch.
A web dashboard hosted on Amazon S3 visualizes energy usage patterns, helping users
optimize energy consumption.”

---
