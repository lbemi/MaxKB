# 使用官方的 PostgreSQL 镜像作为基础镜像
FROM postgres:16.2-bookworm

# 安装必要的依赖
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    postgresql-server-dev-all

# 克隆 `pgvector` 仓库
RUN git clone --branch v0.6.2 https://github.com/pgvector/pgvector.git && \
    cd pgvector && \
    make && \
    make install
