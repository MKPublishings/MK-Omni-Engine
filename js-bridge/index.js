// index.js
// Node.js Express and WebSocket server for MK-Omni-Engine js-bridge

const express = require('express');
const http = require('http');
const WebSocket = require('ws');

const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

// Simple REST endpoint
app.get('/', (req, res) => {
  res.json({ message: 'Hello from Omni JS Bridge!' });
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({ status: 'ok', uptime: process.uptime() });
});

// WebSocket connection
wss.on('connection', function connection(ws) {
  ws.send('WebSocket connected to Omni JS Bridge');
  ws.on('message', function incoming(message) {
    // Echo message for demo
    ws.send(`Echo from server: ${message}`);
  });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
  console.log('WebSocket server enabled');
});
