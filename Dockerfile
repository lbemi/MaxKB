
FROM node:22-alpine as web-build
COPY ui ui
RUN cd ui && \
    npm config set registry https://registry.npmmirror.com/ && \
    npm install &&  \
    npm run build && \
    rm -rf .node_modules

FROM python:3.11-slim-bookworm
# mkdir -p /usr/local/share/model
COPY . /opt/app
# COPY /usr/local/share/model/* /usr/local/share/model/
COPY --from=web-build ui /opt/app/ui
WORKDIR /opt/app
ENV LANG=en_US.UTF-8 \
    PATH=/opt/py3/bin:$PATH \
    LOCAL_MODEL_HOST=127.0.0.1 \
    LOCAL_MODEL_PORT=11636 \
    LOCAL_MODEL_PROTOCOL=http
RUN python3 -m venv /opt/py3 && \
    pip install poetry --break-system-packages && \
    poetry config virtualenvs.create false && \
    . /opt/py3/bin/activate && \
    if [ "$(uname -m)" = "x86_64" ]; then sed -i 's/^torch.*/torch = {version = "^2.2.1+cpu", source = "pytorch"}/g' pyproject.toml; fi && \
    cp /opt/app/installer/config.yaml /usr/local/share/config.yml && \
    rm -rf /opt/app/poetry.lock && \
    poetry install && \
    chmod 755 /opt/app/installer/run-app.sh && \
    cp -f /opt/app/installer/run-app.sh /usr/bin/run-app.sh

EXPOSE 8080
ENTRYPOINT ["bash", "-c"]
CMD [ "/usr/bin/run-app.sh" ]