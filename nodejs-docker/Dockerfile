FROM node:22-alpine

WORKDIR /app

COPY package.json ./
COPY src ./src

RUN npm install

CMD ["node", "src/server.js"]

# ******************************************
# FROM node:22-alpine

# COPY package.json /app/
# COPY src /app/

# RUN npm install

# CMD ["node", "server"]


##### > docker build -t node-server .