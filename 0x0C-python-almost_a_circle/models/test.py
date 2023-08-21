
    def update(self, *args, **kwargs):
        """updates the attributes in a list *args or **kwargs

        Args:
            *args (list): non-keyworded argument list
            **kwargs (dict): keyworded argument list
        """
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.width = a
                elif i == 2:
                    self.height = a
                elif i == 3:
                    self.x = a
                elif i == 4:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns a dictionary representation of a Rectangle instance"""
        new_dict = {}
        new_dict["id"] = self.id
        new_dict["width"] = self.width
        new_dict["height"] = self.height
        new_dict["x"] = self.x
        new_dict["y"] = self.y
        return new_dict


    def area(self):
        """Area of the rectangle instance

        Return:
            the area of the current rectangle instance
        """
        return self.__width * self.__height
