# This Dockerfile gathers all image definitions for pydpf-core needs

# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG DEVCONTAINER_VARIANT="3.10-bullseye"
ARG DPF_SERVER_BASE_IMAGE="rockylinux:8.9-minimal"

# Unzip the server in a separate build stage, so that the final image
# does not contain the 'unzip' package and the '.zip' files.
FROM ubuntu AS unzipper

    SHELL [ "/bin/bash", "-c" ]

    ARG DPF_SERVER_VERSION=''

    ENV ENV_FILE=/ansys_inc/.env

    WORKDIR /ansys_inc

    #RUN mkdir -p /tmp/ansys_inc
    COPY standalones/*dpf*v${DPF_SERVER_VERSION:-*}.zip /tmp/ansys_inc/

    # Deducing DPF_VERSION, DPF_PRE_VERSION and FULL_UNDERSCORE_VERSION from zip name and putting them into environment variables file
    # grep is based on the ARG given (DPF_SERVER_VERSION) if set and not empty, otherwise it looks for any version and we take the first
    # in alphabetical order
    RUN echo "export SERVER_ZIP_NAME=$(ls /tmp/ansys_inc | grep -E ".*dpf.*v${DPF_SERVER_VERSION:-[0-9]+}.*\.zip" | head -1)" > $ENV_FILE \
        && source $ENV_FILE \
        # Looks for {MAJOR}.{MINOR}.{PREVERSION} with  optional PREVERSION (along with leading dot)
        && echo $SERVER_ZIP_NAME | sed -r 's/.*([0-9]{2}\.[12](\.pre[0-9]+)?).*/export FULL_VERSION=\1/g' >> $ENV_FILE \
        && source $ENV_FILE \
        && echo $FULL_VERSION | sed -r 's/.*([0-9]{2}\.[12])\.?(pre[0-9]+)?.*/export DPF_VERSION=\1\nexport DPF_PRE_VERSION=\2/g' >> $ENV_FILE \
        && source $ENV_FILE \
        && echo $DPF_VERSION | sed -e 's/\.//g' -e 's/^/export DPF_VERSION_NO_DOT=/g' >> $ENV_FILE \
        # Transforms the DPF version and DPF_PRE_VERSION (if any) to century version with underscore
        && echo ${DPF_VERSION}${DPF_PRE_VERSION:+.$DPF_PRE_VERSION} | sed -e 's/\./_/g' -e 's/^/export FULL_UNDERSCORE_VERSION=20/g' >> $ENV_FILE \
        && source $ENV_FILE \
        && echo "export WORKDIR=/ansys_inc/ansys/dpf/server_${FULL_UNDERSCORE_VERSION}/aisol/bin/linx64" >> $ENV_FILE

    # Install 7zip
    RUN apt-get update && apt-get install -y p7zip-full

    # Unzipping the server & setting the executable permissions
    RUN source $ENV_FILE && 7z x -y /tmp/ansys_inc/$SERVER_ZIP_NAME -o/ansys_inc \
        && chmod +x $WORKDIR/Ans.Dpf.Grpc.{sh,exe}


FROM ${DPF_SERVER_BASE_IMAGE} AS dpf_server

    ENV TEMP /tmp
    ENV DOCKER_SERVER_PORT 50052
    ENV ENV_FILE /ansys_inc/.env

    LABEL org.opencontainers.image.title="dev-dpf-server"
    LABEL org.opencontainers.image.vendor="Ansys Inc."
    LABEL org.opencontainers.image.description="Development image based on arbitrary archive. For internal use only!"

    EXPOSE ${DOCKER_SERVER_PORT}/tcp

    RUN mkdir -p $TEMP

    COPY --from=unzipper /ansys_inc /ansys_inc

    RUN . $ENV_FILE && echo "export AWP_ROOT${DPF_VERSION_NO_DOT}=$(ls /ansys_inc/ansys/dpf)"

    ENTRYPOINT . $ENV_FILE && cd $WORKDIR && ./Ans.Dpf.Grpc.sh --port ${DOCKER_SERVER_PORT}


# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.245.0/containers/python-3/.devcontainer/base.Dockerfile
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${DEVCONTAINER_VARIANT} AS devcontainer

    ARG USERNAME="vscode"

    COPY --from=unzipper /ansys_inc /dpf_standalone

    # Keep bash history (see https://code.visualstudio.com/remote/advancedcontainers/persist-bash-history)
    RUN KEEP_BASH_HISTORY="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
    && mkdir /commandhistory \
    && touch /commandhistory/.bash_history \
    && chown -R $USERNAME /commandhistory \
    && echo "$KEEP_BASH_HISTORY" >> "/home/$USERNAME/.bashrc"

    # Getting ownership of dpf standalone for current user
    # and ownership for python site-packages
    RUN chown -R $USERNAME /dpf_standalone \
        && mkdir -p /home/$USERNAME/.local/lib \
        && chown -R $USERNAME:$USERNAME /home/$USERNAME

# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
    RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
        # Installs libraries for visualization ("libgl1-mesa-dev" installs "libx11-dev" & "libxrender-dev" as well)
        && apt-get -y install --no-install-recommends libgl1-mesa-dev 

# [Optional] Uncomment this line to install global node packages.
# RUN su vscode -c "source /usr/local/share/nvm/nvm.sh && npm install -g <your-package-here>" 2>&1