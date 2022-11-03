from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox


class CustomDoubleSpinBox(QDoubleSpinBox):

    def validate(self, text: str, pos: int) -> object:
        text = text.replace(".", ",").replace(self.suffix(), "")
        return super(CustomDoubleSpinBox, self).validate(text, pos)

    def valueFromText(self, text: str) -> float:
        text = text.replace(",", ".").replace(self.suffix(), "")
        return float(text)
