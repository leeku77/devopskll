import fire

def hello(name="World"):
    """Prints a greeting message."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    fire.Fire(hello)