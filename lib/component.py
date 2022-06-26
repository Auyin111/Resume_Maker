import matplotlib.pyplot as plt
from lib.element import header, sub_header, RelativeYPerLine, desc, skill_desc, time_period


class Component:

    def __init__(self, header_x, header_y,
                 list_dict_content):

        x = header_x
        y = header_y
        list_default_property = ['indent', 'fontsize', 'weight', 'color', 'url']
        list_non_plt_parmas = ['indent', 'element']
        org_element = None

        for dict_content in list_dict_content:

            element = dict_content['element']
            if org_element is not None:
                # update y
                y -= self.__find_relative_y_per_line(org_element, element) \
                     * self.__find_line_of_str(dict_content['text'])

            dict_content = self.__load_default_property(list_default_property, dict_content, element)
            dict_content['xy'] = (x + header.indent + dict_content['indent'], y)
            # remove parmas not belong to plt
            for parmas in list_non_plt_parmas:
                dict_content.pop(parmas)

            # follow element property if dict_content is None
            plt.annotate(**dict_content)
            
            # set current element as original element
            org_element = element

        self.last_y = y

    @staticmethod
    def __find_relative_y_per_line(org_element, next_element):
        """find the relative by consider the org_element and next_element"""

        # specific element to specific element
        if (org_element == header) & (next_element == sub_header):
            return RelativeYPerLine.header_to_sub_header
        elif (org_element == sub_header) & (next_element == sub_header):
            return RelativeYPerLine.sub_header_to_sub_header
        elif (org_element == desc) & (next_element == sub_header):
            return RelativeYPerLine.desc_to_sub_header
        elif (org_element == skill_desc) & (next_element == sub_header):
            return RelativeYPerLine.skill_desc_to_sub_header
        # any element to specific element
        elif next_element == desc:
            return RelativeYPerLine.to_description
        elif next_element == time_period:
            return RelativeYPerLine.to_time_period
        elif next_element == skill_desc:
            return  RelativeYPerLine.to_skill_description
        else:
            raise Exception(f'can not find relative y between org_element: '
                            f'{org_element.__class__} and  next_element: {next_element.__class__}')

    @staticmethod
    def __find_line_of_str(text):
        """find number of line of a specific string"""

        return len(text.split('\n'))

    @staticmethod
    def __load_default_property(list_default_property, dict_content, element):
        """load default property if not exist in original dict_content"""

        for index, df_property in enumerate(list_default_property):
            str_df_property = list_default_property[index]
            if str_df_property not in dict_content:
                dict_content[str_df_property] = getattr(element, str_df_property)

        return dict_content

