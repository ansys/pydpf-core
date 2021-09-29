# FROM centos:latest
FROM centos:7

MAINTAINER Alex Kaszynski "alexander.kaszynski@ansys.com"

RUN mkdir -p /ansys_inc
COPY v212 /ansys_inc/v212

EXPOSE 50054
WORKDIR /ansys_inc/v212/aisol/bin/linx64/
CMD ["./Ans.Dpf.Grpc.sh"]