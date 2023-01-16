

FROM node:lts-alpine

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy app source code
COPY . .

# Expose the default Docsify port
EXPOSE 3000

# Start the Docsify server
CMD ["npm", "start"]
