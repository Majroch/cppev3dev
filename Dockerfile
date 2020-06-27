FROM ubuntu

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get dist-upgrade -y && \
    apt-get install -y openssh-client git sshpass python3 python3-pip g++-arm-linux-gnueabi && \
    apt-get autoremove -y && \
    apt-get clean

RUN git clone https://github.com/Majroch/cppev3dev.git -o cppev3dev
RUN pip3 install -r /cppev3dev/requirements_linux.txt

CMD ["/cppev3dev/cppev3dev.py"]