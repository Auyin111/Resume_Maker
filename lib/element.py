from abc import ABC, abstractmethod


class Element(ABC):

    def __init__(self):
        self._set_own_property()

    @abstractmethod
    def _set_own_property(self):
        pass


class Header(Element):

    def _set_own_property(self, indent=0, fontsize=12, weight='bold', color=None, url=None):
        self.indent = indent
        self.fontsize = fontsize
        self.weight = weight
        self.color = color
        self.url = url


class SubHeader(Element):

    def _set_own_property(self, indent=0.02, fontsize=10, weight='bold', color=None, url=None):
        self.indent = indent
        self.fontsize = fontsize
        self.weight = weight
        self.color = color
        self.url = url


class WorkingPeriod(Element):

    def _set_own_property(self, indent=0.02, fontsize=9.2, weight=None, color=None, url=None):
        self.indent = indent
        self.fontsize = fontsize
        self.weight = weight
        self.color = color
        self.url = url


class Description(Element):

    def _set_own_property(self, indent=0.04, fontsize=9.2, weight=None, color=None, url=None):
        self.indent = indent
        self.fontsize = fontsize
        self.weight = weight
        self.color = color
        self.url = url


class SkillDescription(Element):

    def _set_own_property(self, indent=0.04, fontsize=8.25, weight=None, color=None, url=None):
        self.indent = indent
        self.fontsize = fontsize
        self.weight = weight
        self.color = color
        self.url = url


class RelativeYPerLine:
    """define the relative y per line of text"""

    # component to component
    comp_to_comp = 0.032
    header_to_sub_header = 0.02
    sub_header_to_sub_header = 0.027
    desc_to_sub_header = 0.02
    # any element to time_period
    to_time_period = 0.015
    # any element to description
    to_description = 0.0135
    to_skill_description = 0.011
    skill_desc_to_sub_header = 0.02
    small_gap = 0.015


header = Header()
sub_header = SubHeader()
time_period = WorkingPeriod()
desc = Description()
skill_desc = SkillDescription()