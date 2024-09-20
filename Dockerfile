FROM nikolaik/python-nodejs

WORKDIR /home/node

COPY . .

RUN curl -sSL https://install.python-poetry.org | python3 -

RUN apt-get install openscad

RUN npm run setup
RUN npm run build

EXPOSE 80

CMD ["npm", "run", "start"]