# stage1 - build react app first 
FROM node:10.19.0 as build
ARG REACT_APP_API_URL
ENV REACT_APP_API_URL=${REACT_APP_API_URL}
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY . /app
RUN yarn build

# stage 2 - build the final image and copy the react build files
FROM nginx:1.17.8-alpine
COPY --from=build /app/build /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/conf.d
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]