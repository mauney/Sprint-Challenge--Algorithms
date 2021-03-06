class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort_bubble_oneway(self):
        """
        Sort the robot's list.
        """
        # make sure light is off
        self.set_light_off()

        # outer loop:
        # check if light is on == sorted list; end loop if so
        while not self.light_is_on():
            # move left to beginning
            while self.can_move_left():
                self.move_left()
            # once at start, turn light on
            self.set_light_on()

            # inner loop: stop when robot reaches end of list
            while self.can_move_right():
                # pick up item
                self.swap_item()
                # move right
                self.move_right()
                # compare items
                if self.compare_item() == 1:
                    # swap if necessary, and turn light off if swapped
                    self.swap_item()
                    self.set_light_off()
                # move left
                self.move_left()
                # place item
                self.swap_item()
                # move right
                self.move_right()
        
        return

    def sort_bubble(self):
        """
        Sort the robot's list.
        """
        # start with light on for sorted list until proven otherwise
        self.set_light_on()

        # outer loop:
        while True:

            # inner loop moving right: stop when robot reaches end of list
            while self.can_move_right():
                # pick up item
                self.swap_item()
                # move right
                self.move_right()

                # check if this is the last compare for this cycle
                # n.b. this is an ugly hack to save one time increase per cycle
                if not self.can_move_right():
                    # compare items
                    if self.compare_item() == 1:
                        # swap if necessary, and turn light off if swapped
                        self.swap_item()
                        self.set_light_off()
                    # move left
                    self.move_left()
                    # place item
                    self.swap_item()
                    break

                # compare items
                if self.compare_item() == 1:
                    # swap if necessary, and turn light off if swapped
                    self.swap_item()
                    self.set_light_off()
                # move left
                self.move_left()
                # place item
                self.swap_item()
                # move right
                self.move_right()
            
            # check light and either break or reset
            if self.light_is_on():
                return # list is sorted
            else:
                self.set_light_on()

            # inner loop moving left: stop when robot reaches start of list
            while self.can_move_left():
                # pick up item
                self.swap_item()
                # move left
                self.move_left()

                # check if this is the last compare for this cycle
                # n.b. this is an ugly hack to save one time increase per cycle
                if not self.can_move_left():
                    # compare items
                    if self.compare_item() == -1:
                        # swap if necessary, and turn light off if swapped
                        self.swap_item()
                        self.set_light_off()
                    # move right
                    self.move_right()
                    # place item
                    self.swap_item()
                    break

                # compare items
                if self.compare_item() == -1:
                    # swap if necessary, and turn light off if swapped
                    self.swap_item()
                    self.set_light_off()
                # move right
                self.move_right()
                # place item
                self.swap_item()
                # move left
                self.move_left()

            # check light and either break or reset
            if self.light_is_on():
                return # list is sorted
            else:
                self.set_light_on()
        
        return

    def sort_selection(self):
        """
        Sort the robot's list.
        """
        self.swap_item()

        while True:
            # move to the right and find our smallest item that hasn't been sorted
            while self.can_move_right():
                self.move_right()
                if self.compare_item() > 0:
                    self.swap_item()
            # if the item is at the end of the list and all items are sorted we are finished
            if self.compare_item() is None:
                self.swap_item()
                return
            else:
                # find spot in list with None, place item in that position, move right and swap
                while self.move_left():
                    if self.compare_item() is None:
                        self.swap_item()
                        self.move_right()
                        self.swap_item()
                        break

    def sort_insertion(self):
        """
        Sort the robot's list.
        """
        # stop when last item has been inserted
        while self.can_move_right():
        # move right and pick up item
            self.move_right()
            self.swap_item()
        # move left to find place to insert
            while self.can_move_left():
                self.move_left()
                # if robot item is greater or equal to position item
                # or robot is at far left position
                if self.compare_item() > -1 or self.can_move_left() == False:
                    # swap items if needed (possible far left condition)
                    if self.compare_item() == -1:
                        self.swap_item()
                    # swap items moving right up to empty spot
                    while self.compare_item() is not None:
                        self.move_right()
                        self.swap_item()
                    break

        return

    def sort(self):
        """
        Sort the robot's list.
        This is a copyt of sort_insertion()
        """
        # stop when last item has been inserted
        while self.can_move_right():
        # move right and pick up item
            self.move_right()
            self.swap_item()
        # move left to find place to insert
            while self.can_move_left():
                self.move_left()
                # if robot item is greater or equal to position item
                # or robot is at far left position
                if self.compare_item() > -1 or self.can_move_left() == False:
                    # swap items if needed (possible far left condition)
                    if self.compare_item() == -1:
                        self.swap_item()
                    # swap items moving right up to empty spot
                    while self.compare_item() is not None:
                        self.move_right()
                        self.swap_item()
                    break

        return


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]
    
    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)