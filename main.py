from agents.writer import WriterAgent
from agents.editor import EditorAgent


def run_pipeline(topic: str):

    writer = WriterAgent()
    editor = EditorAgent()

    print("\n" + "=" * 60)
    print("MULTI-AGENT WRITER → EDITOR PIPELINE")
    print("=" * 60)

    # Agent 1
    print("\n[Agent 1 - Writer] Generating draft...\n")

    draft = writer.write(topic)

    print("WRITER DRAFT:")
    print("-" * 60)
    print(draft)

    # Agent 2
    print("\n[Agent 2 - Editor] Reviewing and improving draft...\n")

    final_output = editor.edit(draft)

    print("EDITOR FINAL OUTPUT:")
    print("-" * 60)
    print(final_output)

    return draft, final_output


if __name__ == "__main__":

    topic = input("Enter a topic: ")

    run_pipeline(topic)