import re


replacements = {
    "sin": "np.sin",
    "cos": "np.cos",
    "exp": "np.exp",
    "sqrt": "np.sqrt",
    "^": "**",
}

allowed_words = [
    "x",
    "sin",
    "cos",
    "sqrt",
    "exp",
]


class Equation:
    def __init__(self, func: str) -> None:
        self._func = func

    def convert(self):
        """
        example: -2x^2 - 6*x + 2 => -2*x**2-6*x+2


        """
        for word in re.findall("[a-zA-Z_]+", self._func):
            if word not in allowed_words:
                raise ValueError('"{}" is forbidden to use in math expression'.format(word))

        cfunc = self._func
        cfunc = cfunc.replace(" ", "")
        cfunc = list(cfunc)
        counter = len(cfunc) - 1
        i = 0
        while i < counter:
            if cfunc[i + 1] == "x" and cfunc[i] in "0123456789":
                cfunc.insert(i + 1, "*")
                counter += 1
            i += 1
        cfunc = "".join(cfunc)

        for old, new in replacements.items():
            cfunc = cfunc.replace(old, new)

        def func(x):
            return eval(cfunc)

        return func

