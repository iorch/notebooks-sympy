FROM jupyter/base-notebook:python-3.9.7

#USER root

USER jovyan

RUN mkdir /tmp/certs

COPY ["server_cert.cnf", "."]
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -config server_cert.cnf -keyout /tmp/certs/mykey.key -out /tmp/certs/mycert.pem

COPY ["requirements.txt", "."]

RUN mamba install --yes --file requirements.txt
RUN set -x && \
    arch=$(uname -m) && \
    if [ "${arch}" == "x86_64" ]; then \
        mamba install --quiet --yes \
            'cadabra2' && \
            mamba clean --all -f -y && \
            fix-permissions "${CONDA_DIR}" && \
            fix-permissions "/home/${NB_USER}"; \
    fi;
RUN conda update -y -n base conda

ARG JUPYTER_PASSWORD
ENV JUPYTER_PASSWORD $JUPYTER_PASSWORD

COPY ["jupyter_notebook_config.py", "./jupyter_notebook_config.py.tmp"]

COPY ["protect_notebook.sh", "."]

RUN ./protect_notebook.sh

EXPOSE 1443
