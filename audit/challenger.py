#!/usr/bin/env python3
"""CHALLENGER — independent pre-ship reviewer (the Rebels mechanic, made real).
Reviews an action against the DA rulebook via a DIFFERENT model (deepseek lane via router),
returns PASS or FLAGs with rule references + reasons. Run: challenger.py <action-json>.
Also supports --retro <file> to review recorded actions (morning sweep uses the ledger)."""
import json, os, pathlib, subprocess, sys, time, urllib.request

# Fleet-internal jump host — set in the deployment env, never committed as a literal
JUMP_HOST = os.environ.get("JUMP_HOST", "jump-host-internal")

RULES = [
    ("R1", "capacity utilization — any owned asset that can work must be working"),
    ("R2", "continuous over batched — no artificial cadence without a real constraint"),
    ("R3", "parallel sources — independent sources run in parallel, not fallback-only"),
    ("R4", "derived deadlines — every deadline = effort/machine-hours ÷ measured lane rate"),
    ("R5", "machine time — scheduling and reporting in machine-hours, not human days"),
    ("R6", "probe-gated — model/lane/tool changes ship with a machine-checkable probe verdict"),
    ("R7", "visible output — every action produces a receipt; silent degradation is a violation"),
    ("R8", "no-khalid-bottleneck — in-bounds work self-executes; waiting on redundant signatures is a violation"),
    ("R9", "independent challenge — no self-review; every ledger-worthy action gets an independent review"),
]

def invoke_lane(action_desc, rulebook):
    payload = json.dumps({"lane_id": "deepseek-api", "payload": {"messages": [
        {"role": "system", "content": (
            "You are the fleet CHALLENGER — an independent quality gate. You review proposed actions "
            "against the DA rulebook and flag violations BEFORE they ship. You are adversarial and "
            "specific. Reply ONLY with JSON: {\"verdict\": \"PASS\"|\"FLAG\", \"flags\": [{\"rule\": \"R1\", "
            "\"reason\": \"...\"}], \"summary\": \"one line\"}. Flag every violation you can find; "
            "PASS only when nothing in the action violates the rules. Do not be lenient.")},
        {"role": "user", "content": f"RULEBOOK:\n{rulebook}\n\nACTION TO REVIEW:\n{action_desc}"}]}}).encode()
    # via the proven helper chain (my box -> brick -> OVH router -> deepseek lane)
    cmd = "ssh -o BatchMode=yes -o ConnectTimeout=8 root@%s 'bash /root/invoke_free.sh'" % JUMP_HOST
    for attempt in range(3):
        p = subprocess.run(["bash", "-c", cmd], input=payload, capture_output=True, timeout=120)
        out = p.stdout.decode(errors="replace").strip()
        try:
            d = json.loads(out)
            if d.get("status") == 200:
                comp = json.loads(d["response"])
                return comp.get("choices", [{}])[0].get("message", {}).get("content", "")
        except Exception:
            pass
        time.sleep(20)
    return None

def review(action_desc):
    rulebook = "\n".join(f"{r}: {d}" for r, d in RULES)
    raw = invoke_lane(action_desc, rulebook)
    if not raw:
        return {"verdict": "CHALLENGER-UNAVAILABLE", "flags": [], "summary": "challenger lane failed"}
    try:
        # strip fences
        s = raw.strip()
        if s.startswith("```"):
            s = s.split("\n", 1)[1].rsplit("```", 1)[0]
        return json.loads(s)
    except Exception:
        return {"verdict": "CHALLENGER-PARSE-ERR", "flags": [], "summary": raw[:200]}

def main():
    if len(sys.argv) < 2:
        print("usage: challenger.py '<action description>' | challenger.py --retro <actions.jsonl>")
        return
    if sys.argv[1] == "--retro":
        total_flags = 0
        for line in open(sys.argv[2]).read().splitlines():
            if not line.strip():
                continue
            act = json.loads(line)
            v = review(act["action"])
            mark = "FLAG" if v.get("verdict") == "FLAG" else v.get("verdict", "?")
            print(f"[{mark}] {act.get('id', '?')}: {act['action'][:80]}")
            for f in v.get("flags", []):
                print(f"      - {f.get('rule')}: {f.get('reason', '')[:140]}")
                total_flags += 1
        print(f"--- retro done: {total_flags} flags total ---")
    else:
        v = review(sys.argv[1])
        print(json.dumps(v, indent=1))

if __name__ == "__main__":
    main()
