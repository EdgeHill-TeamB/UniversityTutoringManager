FROM node:20.11.1

# copy package.json and package-lock.json into /usr/app
WORKDIR /usr/app1

COPY package*.json ./

RUN npm install

RUN ls


COPY . .

EXPOSE 3000

# start the development server
CMD ["npm", "start"]