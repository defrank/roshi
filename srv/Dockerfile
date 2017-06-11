FROM nginx:1.13-alpine

MAINTAINER Derek M. Frank <derek at frank dot sh>
WORKDIR /etc/nginx

COPY conf.d ./

CMD ["nginx", "-c", "conf.d/default.conf"]
