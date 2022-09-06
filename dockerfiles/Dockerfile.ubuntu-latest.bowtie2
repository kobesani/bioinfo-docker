FROM ubuntu:22.04

USER root

RUN apt-get update \
    && apt-get install -yq --no-install-recommends \
        curl \
        python3.10 \
        gcc \
        make \
        ca-certificates \
        unzip \
        zstd \
        zlib1g-dev \
        g++ \
        perl \
        dialog \
        apt-utils \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN useradd --create-home bowtie.user

RUN curl -L "https://github.com/BenLangmead/bowtie2/archive/refs/tags/v2.4.5.zip" \
    -o /tmp/bowtie2-2.4.5-linux-x86_64.zip

RUN mkdir /opt/build && unzip /tmp/bowtie2-2.4.5-linux-x86_64.zip -d /opt/build

RUN cd /opt/build/bowtie2-2.4.5 && make

RUN mkdir /opt/build/scripts

COPY ./scripts/entrypoint_bowtie2.sh /opt/build/scripts

RUN chmod +x /opt/build/scripts/entrypoint_bowtie2.sh

RUN chown -R bowtie.user:bowtie.user /opt/build

USER bowtie.user

ENTRYPOINT [ "/opt/build/scripts/entrypoint_bowtie2.sh" ]