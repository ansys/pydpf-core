# FROM centos:latest
FROM centos:7

MAINTAINER Alex Kaszynski "alexander.kaszynski@ansys.com"

RUN mkdir -p /ansys_inc
COPY v211 /ansys_inc/v211

EXPOSE 50054
WORKDIR /ansys_inc/v211/aisol/bin/linx64/
CMD ["./run_dpf.sh"]