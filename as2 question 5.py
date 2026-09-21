from abc import ABC, abstractmethod


class FileHandler(ABC):
    """
    Abstract Base Class for file handlers.
    Ensures all subclasses implement read and write methods.
    """

    @abstractmethod
    def read(self, filepath: str) -> str | bytes:
        """Read data from a file."""
        pass

    @abstractmethod
    def write(self, filepath: str, data: str | bytes) -> None:
        """Write data to a file."""
        pass


class TextFileHandler(FileHandler):
    """Concrete subclass for handling text files."""

    def read(self, filepath: str) -> str:
        print(f"Opening {filepath} in text mode...")
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()

    def write(self, filepath: str, data: str) -> None:
        print(f"Writing text data to {filepath}...")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(data)


class BinaryFileHandler(FileHandler):
    """Concrete subclass for handling binary files."""

    def read(self, filepath: str) -> bytes:
        print(f"Opening {filepath} in binary mode...")
        with open(filepath, "rb") as f:
            return f.read()

    def write(self, filepath: str, data: bytes) -> None:
        print(f"Writing binary data to {filepath}...")
        with open(filepath, "wb") as f:
            f.write(data)


# --- Example Usage ---
if __name__ == "__main__":
    # 1. Text File Example
    text_handler = TextFileHandler()
    text_handler.write("example.txt", "Hello, world!")
    text_content = text_handler.read("example.txt")
    print(f"Text Content: {text_content}\n")

    # 2. Binary File Example
    bin_handler = BinaryFileHandler()
    bin_handler.write("example.bin", b"\x48\x65\x6c\x6c\x6f")  # "Hello" in hex bytes
    bin_content = bin_handler.read("example.bin")
    print(f"Binary Content: {bin_content}\n")

    # 3. Enforcement Check
    try:
        # This will raise a TypeError because abstract methods are not implemented
        class IncompleteHandler(FileHandler):
            pass


        handler = IncompleteHandler()
    except TypeError as e:
        print(f"Enforcement working! Error: {e}")
