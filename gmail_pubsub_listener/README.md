# 📧 Gmail PubSub Listener - Real-time Email Processing Service

The Gmail PubSub Listener is a real-time email monitoring service that uses Google Cloud Pub/Sub to receive instant notifications when new emails arrive at the sales account. It processes email events and triggers the Lead Manager agent for immediate response to prospect communications.

## 🚀 Features

- **Real-time Email Monitoring**: Instant notifications via Google Cloud Pub/Sub
- **Gmail API Integration**: Secure access to sales email account
- **Lead Manager Integration**: Automatic triggering of lead management workflows
- **Fallback Cron Mode**: Polling-based backup when Pub/Sub is unavailable
- **Service Account Authentication**: Secure, unattended operation
- **Comprehensive Logging**: Detailed activity tracking and debugging
- **Health Monitoring**: Connection testing and error recovery
- **Thread-safe Processing**: Concurrent message handling
