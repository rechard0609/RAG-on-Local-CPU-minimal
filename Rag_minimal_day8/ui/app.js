const GATEWAY_BASE = "http://localhost:8000";

function $(id) { return document.getElementById(id); }

async function refreshStatus() {
  const el = $("status");
  try {
    const r = await fetch(`${GATEWAY_BASE}/status`);
    const data = await r.json();
    el.textContent = JSON.stringify(data, null, 2);
  } catch (e) {
    el.textContent = `status error: ${e}`;
  }
}

async function sendQuery() {
  const model = $("model").value;
  const maxTokens = Number($("maxTokens").value || 512);
  const temperature = Number($("temp").value || 0.2);
  const prompt = $("prompt").value;

  const respEl = $("resp");
  respEl.textContent = "(running...)";

  try {
    const r = await fetch(`${GATEWAY_BASE}/query`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt, model, max_tokens: maxTokens, temperature })
    });
    const data = await r.json();
    if (!r.ok) {
      throw new Error(data?.detail || JSON.stringify(data));
    }
    respEl.textContent = JSON.stringify(data, null, 2);
  } catch (e) {
    respEl.textContent = `ERROR: ${e}`;
  } finally {
    await refreshStatus();
  }
}

$("btnSend").addEventListener("click", sendQuery);
$("btnStatus").addEventListener("click", refreshStatus);

refreshStatus();
