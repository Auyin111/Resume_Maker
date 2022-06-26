import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from lib.element import header, sub_header, time_period, desc, skill_desc, RelativeYPerLine
from lib.component import Component


# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'

# Text Variables
Name = 'Kyle Au'
ProjectsHeader = 'Git Project'

fig_x = 10
fig_y = 14.285
y_to_x_ratio = fig_y / fig_x
fig, ax = plt.subplots(figsize=(fig_x, fig_y))
# remove x,y axes
plt.axis('off')

hyperlink_color = 'mediumblue'
white_color = '#ffffff'
right_region_color = '#000000'
# set background color
ax.set_facecolor('white')
x_right_region = 0.69
x_left_region = .01

# plot my name
plt.annotate(Name, (.01, .98), weight='bold', fontsize=20)
# plot right info
plt.axvline(x=.99, color=right_region_color, alpha=0.5, linewidth=345)

# add self image
arr_code = mpimg.imread(r'fake_image.png')
imagebox = OffsetImage(arr_code, zoom=0.68)
ab = AnnotationBbox(imagebox, (x_right_region + 0.15, 0.865))
ax.add_artist(ab)


# right region
#################################################################

# plot personal image on right region
information = Component(x_right_region, .718,
                        [
                            {'element': header,
                             'color': white_color,
                             'text': 'Information'},
                            {'element': desc,
                             'text': 'xx-xx-xxxx\nphone: xxxxxxxx\nemail: auyin1111@gmail.com',
                             'color': white_color,
                             },
                            {'element': desc,
                             'text': 'Github: Auyin111 (Link)',
                             'color': hyperlink_color,
                             'url': 'https://github.com/Auyin111/',
                             'weight': 'bold',
                             },
                            {'element': desc,
                             'text': 'Expected salary',
                             'color': white_color,
                             'url': '30k to 35k',
                             'weight': 'bold',
                             },
                        ])

# plot white horizontal line on right region
y_white_line = information.last_y - RelativeYPerLine.small_gap
plt.axhline(y=y_white_line, xmin=0, xmax=1, color=white_color, linewidth=3)

# plot skill on right region
skill = Component(x_right_region, y_white_line - RelativeYPerLine.small_gap * 1.5,
                        [
                            {'element': header,
                             'color': white_color,
                             'text': 'Skill'.upper()},

                            {'element': sub_header,
                             'text': 'Programming language',
                             'color': white_color,
                             },
                            {'element': skill_desc,
                             'text': 'Python, C++, MATLAB',
                             'color': white_color},

                            {'element': sub_header,
                             'text': 'Machine learning',
                             'color': white_color,
                             },
                            {'element': skill_desc,
                             'text': 'Packages: sklearn, imblearn, CatBoost\n'
                                     'Ensemble model: bagging, boosting, stacking\n'
                                     'Estimators: e.g. Random forest, Catboost\n'
                                     'GradientBoosting, logistic regression',
                             'color': white_color},

                            {'element': sub_header,
                             'text': 'Deep learning',
                             'color': white_color},
                            {'element': skill_desc,
                             'text': 'Packages: Pytorch, Keras\n'
                                     'RNN, LSTM, GRU, CNN\n'
                                     'Batch Normalization, multi sample dropout\n'
                                     'Layer Normalization\n'
                                     'Stochastic Weight Averaging (SWA)',
                             'color': white_color},

                            {'element': sub_header,
                             'text': 'NLP',
                             'color': white_color},
                            {'element': skill_desc,
                             'text': 'BERT (deberta, albert, roberta)\n'
                                     'Word2Vec, BOW',
                             'color': white_color},

                            {'element': sub_header,
                             'text': 'Data visualization',
                             'color': white_color},
                            {'element': skill_desc,
                             'text': 'Package: wandb, tensorboard, sns\n'
                                     'plotly (include dash)\n'
                                     'Software: Tableau, Qlikview',
                             'color': white_color},

                            {'element': sub_header,
                             'text': 'OS',
                             'color': white_color},
                            {'element': skill_desc,
                             'text': 'linux, Window, IOS',
                             'color': white_color},

                            {'element': sub_header,
                             'text': 'Cloud platform',
                             'color': white_color},
                            {'element': skill_desc,
                             'text': 'Google (GCP), Amazon (AWS)\n'
                                     'Lambdalabs, Paperspace',
                             'color': white_color},

                            {'element': sub_header,
                             'text': 'Version control tool',
                             'color': white_color},
                            {'element': skill_desc,
                             'text': 'Git',
                             'color': white_color},

                            {'element': sub_header,
                             'text': 'Database',
                             'color': white_color},
                            {'element': skill_desc,
                             'text': 'MongoDB, MYSQL, Bigquery, DynamoDB',
                             'color': white_color},

                            {'element': sub_header,
                             'text': 'Container tool',
                             'color': white_color},
                            {'element': skill_desc,
                             'text': 'Docker',
                             'color': white_color},

                            {'element': sub_header,
                             'text': 'Pipeline and scheduler',
                             'color': white_color},
                            {'element': skill_desc,
                             'text': 'Airflow, crontab',
                             'color': white_color},

                            {'element': sub_header,
                             'text': 'Crawling package',
                             'color': white_color},
                            {'element': skill_desc,
                             'text': 'selenium, BeautifulSoup',
                             'color': white_color},

                            {'element': sub_header,
                             'text': 'Other IT skill',
                             'color': white_color},
                            {'element': skill_desc,
                             'text': 'API, OOP',
                             'color': white_color},

                            # less important
                            #######################################
                            {'element': sub_header,
                             'text': 'Campaign management tool',
                             'color': white_color},
                            {'element': skill_desc,
                             'text': 'SAP (marketing cloud), Adobe campaign',
                             'color': white_color},
                        ])

# plot language on right region
language = Component(x_right_region, skill.last_y - RelativeYPerLine.comp_to_comp,
                    [
                        {'element': header,
                         'color': white_color,
                         'text': 'Language'.upper()},

                        {'element': sub_header,
                         'text': 'Cantonese, English, Mandarin',
                         'color': white_color},
                    ])

# left region
#################################################################

# plot introduction on left region
introduction = Component(x_left_region, .95,
                    [
                        {'element': header,
                         'text': 'Introduction'.upper()},

                        {'element': sub_header,
                         'text': 'I am a physics graduate who has a passion in artificial intelligence,\n'
                                 'so I changed my career path three years ago',
                         'fontsize': 11}
                    ])

# plot project on left region
project = Component(x_left_region, introduction.last_y - RelativeYPerLine.comp_to_comp,
                    [
                        {'element': header,
                         'text': 'Public git project'.upper()},

                        {'element': sub_header,
                         'text': 'Kaggle competition - U.S. Patent Phrase to Phrase Matching (Link)',
                         'url': 'https://www.kaggle.com/competitions/us-patent-phrase-to-phrase-matching'
                                '/overview/description',
                         'color': hyperlink_color},
                        {'element': desc,
                         'text': '- The competition is to build a NLP model to predict phrase to phrase similarity'},
                        # TODO: add the hyperlink
                        {'element': desc,
                         'text': '- the workflow of our project:'
                                 '\n    1) crawl the patent context description from website and use it as features'
                                 '\n    2) fine tune different kind of advanced BERT model to predict phrase to phrase'
                                 ' similarity'
                                 '\n    3) try different advanced method from research paper to improve the process'
                                 '\n    4) use the CV stacking ensemble method to improve the prediction from '
                                 'BERT model'},
                        {'element': desc,
                         'text': '- Competition ranking is 526/1889 teams (top 27.8%) (Link)',
                         'color': hyperlink_color,
                         'url': 'https://www.kaggle.com/auyin111/competitions?tab=completed',
                         'weight': 'bold'},
                        {'element': desc,
                         'text': '- link of git repository',
                         'color': hyperlink_color,
                         'url': 'https://github.com/Auyin111/kaggle_patent_competition',
                         'weight': 'bold'},

                        {'element': sub_header,
                         'text': 'Resume maker (Link)'},
                        {'element': desc,
                         'text': '- Generate the CV automatically by python code'},
                        {'element': desc,
                         'text': '- Upload this project in Git is aim to demo coding skill (Link)',
                         'color': hyperlink_color,
                         'url': 'https://github.com/Auyin111/resume_maker',
                         'weight': 'bold'}
                    ])

# plot experience on left region
experience = Component(x_left_region, project.last_y - RelativeYPerLine.comp_to_comp,
                       [
                           {'text': 'Job experience'.upper(),
                            'element': header},

                           {'element': sub_header,
                            'text': 'xxxxxxxx - xxxxxxxxxxxxxxxx'},
                           {'element': time_period,
                            'text': 'xxxxxx - xxxxxx'},
                           {'element': desc,
                            'text': '- xxxxxxxxxxxxxxxx'
                                    '\n- xxxxxxxxxxxxxxxx'
                                    '\n- xxxxxxxxxxxxxxxx'
                                    '\n- xxxxxxxxxxxxxxxx'
                                    '\n- xxxxxxxxxxxxxxxx'
                                    '\n- xxxxxxxxxxxxxxxx'
                                    '\n  xxxxxxxxxxxxxxxx'},

                           {'element': sub_header,
                            'text': 'xxxxxxxxxxxxxxxx - xxxxxxxxxxxxxxxx'},
                           {'element': time_period,
                            'text': 'xxxxxx - xxxxxx'},
                           {'element': desc,
                            'text': '- xxxxxxxxxxxxxxxx'
                                    '\n- xxxxxxxxxxxxxxxx'
                                    '\n- xxxxxxxxxxxxxxxx'},

                           {'element': sub_header,
                            'text': 'xxxxxxxxxxxxxxxx - xxxxxxxxxxxxxxxx'},
                           {'element': time_period,
                            'text': 'xxxxxx- xxxxxx'},
                           {'element': desc,
                            'text': '- xxxxxxxxxxxxxxxx'
                                    '\n  xxxxxxxxxxxxxxxx'
                                    '\n- xxxxxxxxxxxxxxxx'},

                           {'element': sub_header,
                            'text': 'xxxxxxxxxxxxxxxx - xxxxxxxxxxxxxxxx'},
                           {'element': time_period,
                            'text': 'xxxxxx - xxxxxx'}
                       ])

# plot education on left region
education = Component(x_left_region, experience.last_y - RelativeYPerLine.comp_to_comp,
                      [
                          {'text': 'Education'.upper(),
                           'element': header},

                          {'text': 'MSc in Information Technology (Part Time)- The Hong Kong Polytechnic University',
                           'element': sub_header},
                          {'text': '2019-09 - 2021-08',
                           'element': time_period},
                          {'text': '- ML, NLP, computer vision, Big data, finance and database',
                           'element': desc},

                          {'element': sub_header,
                           'text': ' BSc Applied Physics (First Class Honours) - City University of Hong Kong'},
                          {'element': time_period,
                           'text': '2015-09 - 2017-05'},
                          {'element': desc,
                           'text': '- MATLAB, Thermodynamics, Fluid mechanics, Electromagnetism, Quantum Physics,'
                                   '\n  Solid state and Materials Characterization tech.'},

                          {'element': sub_header,
                           'text': 'Associate Degree in Engineering - Hong Kong Community College (HKCC)'},
                          {'element': time_period,
                           'text': '2013-09 - 2015-05'},
                          {'element': desc,
                           'text': '- C++ language, General Physics, Engineering mathematics, SolidWorks and AutoCAD'},
                      ])

# plot achievement on left region
achievement = Component(x_left_region, education.last_y - RelativeYPerLine.comp_to_comp,
                      [
                          {'text': 'Achievement'.upper(),
                           'element': header},
                          {'text': 'SAP marketing cloud (1902) implementation',
                           'element': sub_header},
                          {'text': 'SAP global certification ',
                           'element': desc},

                          {'text': 'College of Science and Engineering Dean’s list in the semester A of 2016/2017',
                           'element': sub_header},
                          {'element': desc,
                           'text': "City University of Hong Kong Dean's list"},
                          {'element': sub_header,
                           'text': 'College of Science and Engineering Dean’s list in the semester B of 2016/2017'},
                          {'element': desc,
                           'text': "City University of Hong Kong Dean's list"},
                      ])

# plot remark on bottom left region
remark = Component(x_left_region, 0.01,
                      [
                          {'text': 'The whole CV is generated by python code',
                           'element': header, 'alpha': 0.5, 'color': 'gray', 'fontsize':20},
                      ])

plt.show()
fig.savefig('demo_cv.pdf')