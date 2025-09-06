FROM node:22-alpine AS builder

WORKDIR /app

# Install only production dependencies
COPY package*.json ./
RUN npm ci --omit=dev

# Copy source code
COPY . .

# Run the app directly with node
CMD ["node", "server.js"]
