FROM tomcat:9.0-alpine

MAINTAINER masha

WORKDIR /usr/local/tomcat/webapps

RUN apk update && apk add git

RUN git clone https://github.com/MashaPast/may_the_force.git

EXPOSE 8080

CMD ["catalina.sh", "run"]