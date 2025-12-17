# JS Bridge for MK-Omni-Engine

This directory contains a Node.js/TypeScript-based bridge module for the Omni AI Framework.

## Purpose
- Demonstrates integration of additional technology into the Python-based Omni Engine.
- Provides a simple REST API for extensibility, monitoring, and interoperability between Python and JavaScript environments.

## Setup
1. Navigate to this directory:
   ```sh
   cd js-bridge
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Run the server:
   ```sh
   npm start
   ```

## Files
- `package.json`: Node.js project metadata
- `index.js`: Main entry point (server implementation)

## Extend
This bridge can be expanded for further features, such as WebSockets, plugin systems, or communication with the Python core via HTTP, sockets, or message queues.
