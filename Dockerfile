FROM    centos:centos7

RUN     yum update -y && \
        yum install -y epel-release && \
        yum update -y && \
        yum groupinstall -y 'Development Tools' && \
        yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel && \
        yum install -y wget

RUN yum install -y python-pip python-devel

RUN     pip install requests && \
        pip install pytest && \
        pip install allure-pytest

ENV PATH=$PATH:/opt/demo/auto-qa-course/
ENV PYTHONPATH=$PATH

ENV RESULTS_FOLDER=/out

WORKDIR /opt/demo/auto-qa-course/

COPY . /opt/demo/auto-qa-course/

CMD ["bash"]
