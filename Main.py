from humor_engine.pipeline.generator import HumorGenerator

def main():
    print("HumorEngine v2.1 — CLI Mode (Hardened)\n")
    
    p_input = input("Persona (dark/chaotic/dry/aggressive/observational): ").strip()
    # Generator handles validation internally now
    generator = HumorGenerator(persona=p_input)
    print(f"Active Persona: {generator.persona}\n")

    while True:
        topic = input("Topic (or 'quit'): ")
        if topic.lower() == "quit":
            break

        style = input("Style (natural/structured/minimal): ").strip() or "natural"

        joke = generator.generate(topic, style=style)
        print("\n" + joke + "\n")

if __name__ == "__main__":
    main()

