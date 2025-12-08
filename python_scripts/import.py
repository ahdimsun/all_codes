import json

def extract_user_prompts(json_path, output_path="prompts.txt"):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    prompts = []

    # The export is a list of conversations
    for convo in data:
        mapping = convo.get("mapping", {})
        for message_id, node in mapping.items():
            message = node.get("message")
            if not message:
                continue

            author = message.get("author", {}).get("role", "")
            content = message.get("content", {})

            # Only extract user messages
            if author == "user":
                parts = content.get("parts", [])
                text = ""
                for p in parts:
                    if isinstance(p, str):
                        text += p
                    elif isinstance(p, dict) and p.get("content_type") == "text":
                        text += p.get("text", "")
                    elif isinstance(p, dict) and p.get("content_type") == "multimodal_text":
                        # multimodal_text contains several parts, including images + text
                        for inner in p.get("parts", []):
                            if isinstance(inner, str):
                                text += inner
                prompts.append(text.strip())

    # Write all prompts to a text file
    with open(output_path, "w", encoding="utf-8") as f:
        for p in prompts:
            if p:
                f.write(p + "\n\n---\n\n")

    print(f"Done! Extracted {len(prompts)} user prompts into:", output_path)


# Example usage:
extract_user_prompts("/home/ahdimsun/Downloads/59cb11c6545ceafd1e1135d72978025b8f0c1063f47584f3ae7823b018d5f1f0-2025-12-06-07-56-05-024cc8380eb641b6a68430e02dd08670/conversations.json")
