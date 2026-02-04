FROM public.ecr.aws/q6y2q4k8/node:23.11.0-alpine3.21
WORKDIR /app
COPY . .
RUN npm install -g npm@9.7.1
RUN npm install date-utils
RUN npm install --save express
CMD ["node", "src/index.js"]
EXPOSE 80