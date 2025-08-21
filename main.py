# main.py
import sys
import os

# Add current directory to Python path so imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from mcp.coordinator import CoordinatorAgent


def get_transcript():
    if len(sys.argv) > 1 and not sys.argv[1].startswith("--"):
        file_path = sys.argv[1]
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    print("=== Meeting Intelligence Agent (MCP Version) ===\n")
    print("Enter/Paste your meeting transcript below.")
    print("(CTRL+Z + ENTER on Windows OR CTRL+D on Mac/Linux to finish)\n")
    data = sys.stdin.read()
    if not data.strip():
        print("⚠️ No transcript provided. Exiting.")
        sys.exit(1)
    return data

def arg_value(flag: str, default: str):
    for idx, a in enumerate(sys.argv):
        if a == flag and idx + 1 < len(sys.argv):
            return sys.argv[idx + 1]
        if a.startswith(flag + "="):
            return a.split("=", 1)[1]
    return default

def main():
    transcript = get_transcript()
    prefix = arg_value("--prefix", "meeting")
    coordinator = CoordinatorAgent(transcript)
    results = coordinator.run(report_prefix=prefix)

    print("\n=== Final Meeting Report ===\n")
    print("--- Notes ---")
    print(results["notes"])
    print("\n--- Action Items ---")
    print(results["actions"])
    print("\n--- Summary ---")
    print(results["summary"])
    if results["report_path"]:
        print(f"\n📄 Saved Report: {results['report_path']}")
    if results["email_outbox"]:
        print(f"📬 Outbox: {results['email_outbox']}")

if __name__ == "__main__":
    main()
