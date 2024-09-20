FROM node:20-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json ./
RUN npm install

# Copy all files to the container
COPY . .

# Expose port 3000 and start the React development server
EXPOSE 3000
CMD ["npm", "start"]
