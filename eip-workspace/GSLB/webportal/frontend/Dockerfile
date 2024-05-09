# syntax=docker/dockerfile:1

FROM node:16.14.0-alpine3.15 as build

WORKDIR /frontend

COPY ./package*.json ./
RUN yarn install

COPY . .
RUN yarn build

FROM nginx

COPY ./Certs/cert.key /etc/nginx/ssl/nginx-selfsigned.key
COPY ./Certs/cert.crt /etc/nginx/ssl/nginx-selfsigned.crt

COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /frontend/build /usr/share/nginx/html
