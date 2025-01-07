FROM node:22-alpine

WORKDIR /app

COPY package.json ./

RUN npm install

COPY . .

EXPOSE 3000 9229

# CMD ["node", "--inspect=0.0.0.0:9229", "node_modules/.bin/tsx", "watch", "src/index.ts"]

CMD ["npm", "run", "dev"]
