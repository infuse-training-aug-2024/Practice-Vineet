# Use the official Node.js image for the backend
FROM node:20-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json ./
RUN npm install

# Copy all files to the container
COPY . .

# Expose port 5000 and start the Node.js backend server
EXPOSE 5000
CMD ["node", "server.js"]
