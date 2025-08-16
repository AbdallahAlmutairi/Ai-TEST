FROM node:18-alpine
WORKDIR /app
COPY ../../apps/web/package.json ./
RUN npm install
COPY ../../apps/web /app
CMD ["npm", "run", "dev"]
