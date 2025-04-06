import sys
from datetime import datetime

TOPICS_FILE = "topics.txt"

def add_topic(topic):
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    with open(TOPICS_FILE, "a") as f:
        f.write(f"{topic}\n")
    print(f"✅ Added topic: '{topic}' on {timestamp} to {TOPICS_FILE}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("⚠️  Usage: python add_topic.py 'Your learning topic here'")
    else:
        topic = " ".join(sys.argv[1:])
        add_topic(topic)
