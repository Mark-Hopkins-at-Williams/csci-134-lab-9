from trees import TreeNode

class LessThan:

    def __init__(self):
        self.history = []

    def __call__(self, value1, value2):
        """ Replace this with your code for Question One ("Abby"). """

    def report(self):
        result = [tuple(sorted([v1, v2])) for (v1, v2) in self.history]
        self.history = []
        return result

""" 
Oscar's custom-made comparison function. 

Do not delete or change! You'll need this.

"""
lessthan = LessThan()


def bubble_sort(ls):
    """ Adapt this code for Question Two ("Adept"). """
    for goal in range(len(ls), 0, -1):
        for baton in range(0, goal - 1):
            if ls[baton + 1] < ls[baton]:
                ls[baton], ls[baton + 1] = ls[baton + 1], ls[baton]


def pivot_sort(ls):
    """
    Replace this with your code for Question Three ("Choosy").

    Then you'll have to modify it for Question Four ("Hilly"),
    but make sure it still works for Question Three!

    """    


def quick_sort(ls):
    """ This won't work until you implement pivot_sort! """
    from random import randint
    return pivot_sort(ls, lambda ls: randint(0, len(ls) - 1))


def build_tree(ls):
    """ Replace this with your code for Question Five ("Chop"). """


def merge(ls1, ls2):
    """ Replace this with your code for Question Six ("Affix"). """


def bottom_up_merge(tree):
    """ Replace this with your code for Question Seven ("Below"). """


def merge_sort(ls):
    """ This won't work until you implement build_tree and bottom_up_merge! """
    tree = build_tree(ls)
    return bottom_up_merge(tree)


def count_comparisons(sorter, ls):
    lessthan.report()
    sorter(ls)
    return len(lessthan.report())


def plot_efficiency_curve(sorters, max_length, adversarial=False):
    """ Oscar and Skeeter's software for measuring efficiency. """
    from random import shuffle
    from matplotlib.pyplot import plot
    from matplotlib import pyplot
    for sorter in sorters:
        x_coords = list(range(1, max_length + 1))
        y_coords = []
        for x in x_coords:
            ls = list(range(x))
            if not adversarial:
                shuffle(ls)
            y = count_comparisons(sorter, ls)
            y_coords = y_coords + [y]
        plot(x_coords, y_coords, label=sorter.__name__)
    pyplot.legend()
    pyplot.title("Efficiency Curve")
    pyplot.xlabel("Length of list")
    pyplot.ylabel("Number of comparisons")
    pyplot.show()



