FROM ubuntu:22.04

WORKDIR /opt

RUN apt-get update && apt-get install -y --no-install-recommends \
    git cmake build-essential ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# Build llama.cpp server (CPU)
RUN git clone --depth 1 https://github.com/ggerganov/llama.cpp.git
WORKDIR /opt/llama.cpp
RUN cmake -S . -B build -DGGML_OPENMP=ON \
 && cmake --build build -j

WORKDIR /app
COPY ./run.sh /app/run.sh
RUN chmod +x /app/run.sh

ENV MODEL_PATH=/models/model.gguf
ENV N_THREADS=4
ENV N_CTX=2048

EXPOSE 8080

ENTRYPOINT ["/app/run.sh"]
