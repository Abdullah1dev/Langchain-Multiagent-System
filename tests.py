from agents.writer import WriterAgent
from agents.editor import EditorAgent


def run_test(topic: str, number: int):

    writer = WriterAgent()
    editor = EditorAgent()

    print("\n")
    print("=" * 70)
    print(f"TEST {number}")
    print(f"TOPIC: {topic}")
    print("=" * 70)

    # Agent 1
    draft = writer.write(topic)

    print("\n--- AGENT 1: WRITER DRAFT ---")
    print(draft)

    # Agent 2
    final_output = editor.edit(draft)

    print("\n--- AGENT 2: EDITOR FINAL OUTPUT ---")
    print(final_output)

    return draft, final_output


topics = [
    "Explain the importance of Python for becoming an AI engineer.",
    "Explain how Retrieval-Augmented Generation (RAG) works and why it is useful."
]


for index, topic in enumerate(topics, start=1):
    run_test(topic, index)