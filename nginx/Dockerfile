
FROM nginx:latest

COPY /etc /etc
COPY default.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]