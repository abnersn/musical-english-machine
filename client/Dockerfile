FROM node:22.11-alpine AS build

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

COPY . .

RUN npm run build

RUN npm i -g serve

EXPOSE 3000

CMD ["serve", "-s", "dist", "-p", "3000"]