#!/usr/bin/env python3
"""Overnight coord peer ping — A2A jsonrpc envelope. Never prints token values."""
import json, re, subprocess, sys, time

ENV = "/home/bawes/.hermes/.env"

def get_tokens():
    line = [l for l in open(ENV) if l.startswith("A2A_PEER_TOKENS=")][0].strip()
    toks = {}
    for part in line.split("=", 1)[1].split(","):
        k, v = part.split(":", 1)
        toks[k] = v
    return toks

TOK = get_tokens()

def redact(s):
    # redact anything that looks like a bearer token / env token line
    s = re.sub(r'(A2A_PEER_TOKENS=)[^\s"]+', r'\1<REDACTED>', s)
    s = re.sub(r'(Bearer )\S+', r'\1<REDACTED>', s)
    s = re.sub(r'[A-Za-z0-9_-]{40,}', '<TOKLIKE>', s)
    return s

def call(port, tok, method, params, timeout=60):
    body = json.dumps({"jsonrpc": "2.0", "id": int(time.time()*1000) % 1000000,
                       "method": method, "params": params})
    url = f"http://127.0.0.1:{port}/"
    try:
        r = subprocess.run(["curl", "-s", "--max-time", str(timeout), "-w",
                            "\n__HTTP__%{http_code}", "-X", "POST", url,
                            "-H", "Content-Type: application/json",
                            "-H", "Accept: application/json, text/event-stream",
                            "-H", f"Authorization: Bearer {tok}",
                            "-d", body], capture_output=True, text=True, timeout=timeout+10)
        out = r.stdout
        http = "000"
        m = re.search(r"__HTTP__(\d+)\s*$", out)
        if m:
            http = m.group(1)
            out = out[: m.start()]
        return http, redact(out.strip() or r.stderr.strip())
    except Exception as e:
        return "ERR", redact(str(e))

def ping(port, tok, label):
    print(f"=== {label} @ {port} ===")
    # status ping via message/send
    h, b = call(port, tok, "message/send", {"message": {
        "role": "user",
        "parts": [{"text": "status check — reply with anything pending from hermes-local"}]}})
    print(f"[message/send] HTTP {h}")
    print(b[:4000])
    print()
    # also try tasks/get on previously-known task ids (cheap, may 404)
    for tid in ["task-e0b86bd077fe456f", "task-cac2b8f8b321411f"]:
        h, b = call(port, tok, "tasks/get", {"id": tid}, timeout=30)
        print(f"[tasks/get {tid}] HTTP {h}")
        print(b[:1500])
        print()
    return h, b

if __name__ == "__main__":
    agi = ping(19903, TOK["agi"], "AGI")
    brick = ping(19901, TOK["brick"], "BRICK")
    # health check for brick (GET /, no auth needed per prior ticks)
    try:
        r = subprocess.run(["curl", "-s", "--max-time", "15", "-o", "/dev/null", "-w", "%{http_code}",
                            "http://127.0.0.1:19901/"], capture_output=True, text=True, timeout=25)
        print(f"[brick GET /] HTTP {r.stdout}")
    except Exception as e:
        print(f"[brick GET /] ERR {redact(str(e))}")
