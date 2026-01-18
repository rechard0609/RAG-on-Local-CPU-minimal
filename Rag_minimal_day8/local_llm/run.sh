#!/usr/bin/env bash
set -euo pipefail

MODEL_PATH="${MODEL_PATH:-/models/model.gguf}"
N_THREADS="${N_THREADS:-4}"
N_CTX="${N_CTX:-2048}"

if [ ! -f "$MODEL_PATH" ]; then
  echo "[local-llm] ERROR: model file not found: $MODEL_PATH" >&2
  echo "[local-llm] Put a GGUF model under ./models and set MODEL_PATH if needed." >&2
  exit 1
fi

echo "[local-llm] starting llama.cpp server"
echo "[local-llm] model: $MODEL_PATH"
echo "[local-llm] threads: $N_THREADS"
echo "[local-llm] ctx: $N_CTX"

# llama.cpp server binary path
BIN="/opt/llama.cpp/build/bin/llama-server"
if [ ! -x "$BIN" ]; then
  # Older build layouts
  BIN="/opt/llama.cpp/build/bin/server"
fi

if [ ! -x "$BIN" ]; then
  echo "[local-llm] ERROR: server binary not found in build output." >&2
  exit 1
fi

exec "$BIN" \
  --host 0.0.0.0 \
  --port 8080 \
  -m "$MODEL_PATH" \
  -t "$N_THREADS" \
  -c "$N_CTX"
