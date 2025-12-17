FROM node:18-slim

WORKDIR /usr/src/app

# Install dependencies
COPY package.json package-lock.json* ./
RUN npm install --production || npm install

# Copy source
COPY . .

EXPOSE 3000

CMD ["node", "index.js"]
