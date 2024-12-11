from coding_exercise.domain.model.cable import Cable


class Splitter:

    CABLE_MIN_LENGTH = 2
    CABLE_MAX_LENGTH = 1024
    TIMES_MIN = 1
    TIMES_MAX = 1024

    def __init__(self):
        self.longest_int: int = None
        self.result: list[Cable] = []
        self.cable_count: int = 0
        self.length: int = 0

    def __validate(self, cable: Cable, times: int) -> bool:
        """
        Validate the input parameters
        Parameters
        ----------
        cable : Cable
            The cable to be split
        times : int
            The number of times the cable should be split

        Returns
        -------
        None

        """

        if not isinstance(cable, Cable):
            raise TypeError("The cable is not an instance of Cable.")

        if not isinstance(times, int):
            raise TypeError("The times is not an instance of int.")

        if times < self.TIMES_MIN or times > self.TIMES_MAX:
            raise ValueError(
                "Cannot split less than: {self.TIMES_MIN} or more than: {self.TIMES_MAX} times the cable.")

        if cable.length < self.CABLE_MIN_LENGTH or cable.length > self.CABLE_MAX_LENGTH:
            raise ValueError(
                "The cable length should be between: {self.CABLE_MIN_LENGTH} and {self.CABLE_MAX_LENGTH}")

    def __format_cable_name(self, name: str, index: int) -> str:
        """
        Format the cable name in the given format:
        {name}-{index}

        Parameters
        ----------
        name : str
            The name of the cable
        index : int

        Returns
        -------
        str
            The formatted cable name
        """

        pad_width = len(str(len(self.result)))
        return f"{name}-{str(index).zfill(pad_width)}"

    def split(self, cable: Cable, times: int) -> list[Cable]:
        """
        Split the cable into the given number of pieces
        Parameters
        ----------
        cable : Cable
            The cable to be split
        times : int
            The number of times the cable should be split

        Returns
        -------
        list[Cable]
            The list of cables after the split
        """

        self.__validate(cable=cable, times=times)

        self.length = cable.length
        name = cable.name
        inital_sections = times + 1

        equal_length, remainder_length = divmod(self.length, inital_sections)

        # If remainder, check if we can create extra equal sections?
        extra_sections, remainder = divmod(remainder_length, equal_length)

        # Validate the extra sections
        equal_sections = inital_sections + extra_sections

        if remainder:
            self.tolal_sections = equal_sections + 1
        else:
            self.total_sections = equal_sections

        for i in range(self.equal_sections):
            if i < self.equal_sections:
                self.result.append(
                    Cable(
                        self.equal_length,
                        self.__format_cable_name(cable.name, i, self.total_sections),
                    )
                )
            else:
                self.result.append(
                    Cable(
                        self.equal_length + 1,
                        self.__format_cable_name(cable.name, i, self.total_sections),
                    )
                )

        if self.remainder:
            self.result.append(
                Cable(
                    self.equal_length + 1,
                    self.__format_cable_name(
                        cable.name, self.total_sections - 1, self.total_sections
                    ),
                )
            )

        return self.result
