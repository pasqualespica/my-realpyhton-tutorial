
import abc
class InformalParserInterface:
    def load_data_source(self, path: str, file_name: str) -> str:
        """Load in the file for extracting text."""
        pass

    def extract_text(self, full_file_name: str) -> dict:
        """Extract text from the currently loaded file."""
        pass


class PdfParser(InformalParserInterface):
    """Extract text from a PDF"""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides InformalParserInterface.extract_text()"""
        pass


class EmlParser(InformalParserInterface):
    """Extract text from an email"""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override InformalParserInterface.extract_text()
        """
        pass


print("Main...")
print()

# Check if both PdfParser and EmlParser implement InformalParserInterface
print(f"issubclass(PdfParser, InformalParserInterface) {issubclass(PdfParser, InformalParserInterface)}")
print(f"issubclass(EmlParser, InformalParserInterface) {issubclass(EmlParser, InformalParserInterface)}")
print()
# TRUE  --- Al little bit weird !!!!
print("Method Resolution Order(MRO) #1 .. ")
print(PdfParser.__mro__)
print(EmlParser.__mro__)

print("\n ................................................................ \n")


class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text))


class PdfParserNew:
    """Extract text from a PDF."""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass


class EmlParserNew:
    """Extract text from an email."""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        pass


# Check if both PdfParser and EmlParser implement InformalParserInterface
print(issubclass(PdfParserNew, FormalParserInterface))
print(issubclass(EmlParserNew, FormalParserInterface))

# TRUE and FALSE  --- now  !!!!
print("\nMethod Resolution Order(MRO) #2 .. ")
print(PdfParserNew.__mro__)
print(EmlParserNew.__mro__)


pdf_parser = PdfParserNew()
eml_parser = EmlParserNew()


print("\n ................................................................ \n")

class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text) or
                NotImplemented)

    @abc.abstractmethod
    def load_data_source(self, path: str, file_name: str):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def extract_text(self, full_file_path: str):
        """Extract text from the data set"""
        raise NotImplementedError


class PdfParserNew(FormalParserInterface):
    """Extract text from a PDF."""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass


class EmlParserNew(FormalParserInterface):
    """Extract text from an email."""

    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        pass


# Check if both PdfParser and EmlParser implement InformalParserInterface
print(issubclass(PdfParserNew, FormalParserInterface))
print(issubclass(EmlParserNew, FormalParserInterface))

print(PdfParserNew.__mro__)
print(EmlParserNew.__mro__)

pdf_parser = PdfParserNew()
eml_parser = EmlParserNew()
