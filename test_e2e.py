import asyncio
import subprocess
import time
import urllib.request
import json

async def test_server_and_streaming():
    # Start server in background
    proc = subprocess.Popen(["python3", "/home/ubuntu/parakeet-ai-prototype/parakeet_server.py"])
    time.sleep(2)

    try:
        # Test 1: Check UI load
        with urllib.request.urlopen("http://127.0.0.1:8765/index.html") as resp:
            content = resp.read().decode('utf-8')
            assert "Parakeet AI" in content
            assert "Suggest Answer" in content
            print("✅ Test 1 Passed: Desktop UI served correctly.")

        # Test 2: Check STT Endpoint
        req_stt = urllib.request.Request("http://127.0.0.1:8765/api/stt-transcribe", data=b"{}", headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req_stt) as resp:
            stt_data = json.loads(resp.read().decode('utf-8'))
            assert stt_data["status"] == "success"
            print("✅ Test 2 Passed: Speech-to-Text inference endpoint working.")

        # Test 3: Check Progressive LLM Streaming (SSE)
        req_stream = urllib.request.Request(
            "http://127.0.0.1:8765/api/generate-stream",
            data=json.dumps({"prompt": "How does Parakeet AI work?", "model": "llama3.2"}).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        tokens_received = []
        with urllib.request.urlopen(req_stream) as resp:
            for line in resp:
                l = line.decode('utf-8').strip()
                if l.startswith("data: "):
                    d = json.loads(l[6:])
                    if "token" in d:
                        tokens_received.append(d["token"])
                    if d.get("done"):
                        break

        full_streamed_answer = "".join(tokens_received)
        assert len(tokens_received) > 5
        print(f"✅ Test 3 Passed: Progressive LLM stream verified ({len(tokens_received)} chunks received).")
        print(f"Sample Output:\n'{full_streamed_answer[:120]}...'")

    finally:
        proc.terminate()
        proc.wait()
        print("Server shutdown safely.")

if __name__ == '__main__':
    asyncio.run(test_server_and_streaming())
