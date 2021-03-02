{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "_cell_guid": "b1076dfc-b9ad-4769-8c92-a6c4dae69d19",
    "_uuid": "8f2839f25d086af736a60e9eeb907d3b93b6e0e5",
    "colab": {},
    "colab_type": "code",
    "id": "U2D2gTdJVp90"
   },
   "outputs": [],
   "source": [
    "import numpy as np # to call libraries neccessity to complete the project\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "from collections import Counter\n",
    "import datetime as dt\n",
    "import itertools"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "_cell_guid": "79c7e3d0-c299-4dcb-8224-4455121ee9b0",
    "_uuid": "d629ff2d2480ee46fbb7e2d37f6b5fab8052498a",
    "colab": {},
    "colab_type": "code",
    "id": "oyGfxL3eVp9-"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>imdb_id</th>\n",
       "      <th>budget</th>\n",
       "      <th>revenue</th>\n",
       "      <th>original_title</th>\n",
       "      <th>cast</th>\n",
       "      <th>director</th>\n",
       "      <th>tagline</th>\n",
       "      <th>overview</th>\n",
       "      <th>runtime</th>\n",
       "      <th>genres</th>\n",
       "      <th>production_companies</th>\n",
       "      <th>release_date</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>release_year</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>754</th>\n",
       "      <td>tt1436562</td>\n",
       "      <td>90000000</td>\n",
       "      <td>484635760</td>\n",
       "      <td>Rio</td>\n",
       "      <td>Jesse Eisenberg|Anne Hathaway|Leslie Mann|Jane...</td>\n",
       "      <td>Carlos Saldanha</td>\n",
       "      <td>1 out of every 8 Americans is afraid of flying...</td>\n",
       "      <td>Captured by smugglers when he was just a hatch...</td>\n",
       "      <td>96</td>\n",
       "      <td>Animation|Adventure|Comedy|Family</td>\n",
       "      <td>Blue Sky Studios|Twentieth Century Fox Animation</td>\n",
       "      <td>4/3/2011</td>\n",
       "      <td>6.5</td>\n",
       "      <td>2011</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1162</th>\n",
       "      <td>tt0251736</td>\n",
       "      <td>7000000</td>\n",
       "      <td>16829545</td>\n",
       "      <td>House of 1000 Corpses</td>\n",
       "      <td>Sid Haig|Bill Moseley|Sheri Moon Zombie|Karen ...</td>\n",
       "      <td>Rob Zombie</td>\n",
       "      <td>You'll never get out alive.</td>\n",
       "      <td>Two teenage couples traveling across the backw...</td>\n",
       "      <td>89</td>\n",
       "      <td>Horror</td>\n",
       "      <td>Universal Pictures|Spectacle Entertainment Group</td>\n",
       "      <td>4/11/2003</td>\n",
       "      <td>5.8</td>\n",
       "      <td>2003</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>501</th>\n",
       "      <td>tt0126029</td>\n",
       "      <td>60000000</td>\n",
       "      <td>484409218</td>\n",
       "      <td>Shrek</td>\n",
       "      <td>Mike Myers|Eddie Murphy|Cameron Diaz|John Lith...</td>\n",
       "      <td>Andrew Adamson|Vicky Jenson</td>\n",
       "      <td>The greatest fairy tale never told.</td>\n",
       "      <td>It ain't easy bein' green -- especially if you...</td>\n",
       "      <td>90</td>\n",
       "      <td>Adventure|Animation|Comedy|Family|Fantasy</td>\n",
       "      <td>DreamWorks SKG|Pacific Data Images (PDI)|Dream...</td>\n",
       "      <td>5/16/2001</td>\n",
       "      <td>7.1</td>\n",
       "      <td>2001</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1336</th>\n",
       "      <td>tt0360717</td>\n",
       "      <td>207000000</td>\n",
       "      <td>550000000</td>\n",
       "      <td>King Kong</td>\n",
       "      <td>Naomi Watts|Jack Black|Adrien Brody|Thomas Kre...</td>\n",
       "      <td>Peter Jackson</td>\n",
       "      <td>The eighth wonder of the world.</td>\n",
       "      <td>In 1933 New York, an overly ambitious movie pr...</td>\n",
       "      <td>187</td>\n",
       "      <td>Adventure|Drama|Action</td>\n",
       "      <td>WingNut Films|Universal Pictures|Big Primate P...</td>\n",
       "      <td>12/14/2005</td>\n",
       "      <td>6.4</td>\n",
       "      <td>2005</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1463</th>\n",
       "      <td>tt0479143</td>\n",
       "      <td>24000000</td>\n",
       "      <td>155721132</td>\n",
       "      <td>Rocky Balboa</td>\n",
       "      <td>Sylvester Stallone|Burt Young|Milo Ventimiglia...</td>\n",
       "      <td>Sylvester Stallone</td>\n",
       "      <td>It ain't over 'til it's over.</td>\n",
       "      <td>When he loses a highly publicized virtual boxi...</td>\n",
       "      <td>102</td>\n",
       "      <td>Drama</td>\n",
       "      <td>Columbia Pictures|Revolution Studios|Rogue Mar...</td>\n",
       "      <td>12/20/2006</td>\n",
       "      <td>6.4</td>\n",
       "      <td>2006</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        imdb_id     budget    revenue         original_title  \\\n",
       "754   tt1436562   90000000  484635760                    Rio   \n",
       "1162  tt0251736    7000000   16829545  House of 1000 Corpses   \n",
       "501   tt0126029   60000000  484409218                  Shrek   \n",
       "1336  tt0360717  207000000  550000000              King Kong   \n",
       "1463  tt0479143   24000000  155721132           Rocky Balboa   \n",
       "\n",
       "                                                   cast  \\\n",
       "754   Jesse Eisenberg|Anne Hathaway|Leslie Mann|Jane...   \n",
       "1162  Sid Haig|Bill Moseley|Sheri Moon Zombie|Karen ...   \n",
       "501   Mike Myers|Eddie Murphy|Cameron Diaz|John Lith...   \n",
       "1336  Naomi Watts|Jack Black|Adrien Brody|Thomas Kre...   \n",
       "1463  Sylvester Stallone|Burt Young|Milo Ventimiglia...   \n",
       "\n",
       "                         director  \\\n",
       "754               Carlos Saldanha   \n",
       "1162                   Rob Zombie   \n",
       "501   Andrew Adamson|Vicky Jenson   \n",
       "1336                Peter Jackson   \n",
       "1463           Sylvester Stallone   \n",
       "\n",
       "                                                tagline  \\\n",
       "754   1 out of every 8 Americans is afraid of flying...   \n",
       "1162                        You'll never get out alive.   \n",
       "501                 The greatest fairy tale never told.   \n",
       "1336                    The eighth wonder of the world.   \n",
       "1463                      It ain't over 'til it's over.   \n",
       "\n",
       "                                               overview  runtime  \\\n",
       "754   Captured by smugglers when he was just a hatch...       96   \n",
       "1162  Two teenage couples traveling across the backw...       89   \n",
       "501   It ain't easy bein' green -- especially if you...       90   \n",
       "1336  In 1933 New York, an overly ambitious movie pr...      187   \n",
       "1463  When he loses a highly publicized virtual boxi...      102   \n",
       "\n",
       "                                         genres  \\\n",
       "754           Animation|Adventure|Comedy|Family   \n",
       "1162                                     Horror   \n",
       "501   Adventure|Animation|Comedy|Family|Fantasy   \n",
       "1336                     Adventure|Drama|Action   \n",
       "1463                                      Drama   \n",
       "\n",
       "                                   production_companies release_date  \\\n",
       "754    Blue Sky Studios|Twentieth Century Fox Animation     4/3/2011   \n",
       "1162   Universal Pictures|Spectacle Entertainment Group    4/11/2003   \n",
       "501   DreamWorks SKG|Pacific Data Images (PDI)|Dream...    5/16/2001   \n",
       "1336  WingNut Films|Universal Pictures|Big Primate P...   12/14/2005   \n",
       "1463  Columbia Pictures|Revolution Studios|Rogue Mar...   12/20/2006   \n",
       "\n",
       "      vote_average  release_year  \n",
       "754            6.5          2011  \n",
       "1162           5.8          2003  \n",
       "501            7.1          2001  \n",
       "1336           6.4          2005  \n",
       "1463           6.4          2006  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = pd.read_csv('movie_bd_v5.csv') # to read the dataset\n",
    "data.sample(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "CoYUnagMVp-C",
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>budget</th>\n",
       "      <th>revenue</th>\n",
       "      <th>runtime</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>release_year</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>1.889000e+03</td>\n",
       "      <td>1.889000e+03</td>\n",
       "      <td>1889.000000</td>\n",
       "      <td>1889.000000</td>\n",
       "      <td>1889.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>5.431083e+07</td>\n",
       "      <td>1.553653e+08</td>\n",
       "      <td>109.658549</td>\n",
       "      <td>6.140762</td>\n",
       "      <td>2007.860773</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>4.858721e+07</td>\n",
       "      <td>2.146698e+08</td>\n",
       "      <td>18.017041</td>\n",
       "      <td>0.764763</td>\n",
       "      <td>4.468841</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>5.000000e+06</td>\n",
       "      <td>2.033165e+06</td>\n",
       "      <td>63.000000</td>\n",
       "      <td>3.300000</td>\n",
       "      <td>2000.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2.000000e+07</td>\n",
       "      <td>3.456058e+07</td>\n",
       "      <td>97.000000</td>\n",
       "      <td>5.600000</td>\n",
       "      <td>2004.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>3.800000e+07</td>\n",
       "      <td>8.361541e+07</td>\n",
       "      <td>107.000000</td>\n",
       "      <td>6.100000</td>\n",
       "      <td>2008.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>7.200000e+07</td>\n",
       "      <td>1.782626e+08</td>\n",
       "      <td>120.000000</td>\n",
       "      <td>6.600000</td>\n",
       "      <td>2012.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>3.800000e+08</td>\n",
       "      <td>2.781506e+09</td>\n",
       "      <td>214.000000</td>\n",
       "      <td>8.100000</td>\n",
       "      <td>2015.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             budget       revenue      runtime  vote_average  release_year\n",
       "count  1.889000e+03  1.889000e+03  1889.000000   1889.000000   1889.000000\n",
       "mean   5.431083e+07  1.553653e+08   109.658549      6.140762   2007.860773\n",
       "std    4.858721e+07  2.146698e+08    18.017041      0.764763      4.468841\n",
       "min    5.000000e+06  2.033165e+06    63.000000      3.300000   2000.000000\n",
       "25%    2.000000e+07  3.456058e+07    97.000000      5.600000   2004.000000\n",
       "50%    3.800000e+07  8.361541e+07   107.000000      6.100000   2008.000000\n",
       "75%    7.200000e+07  1.782626e+08   120.000000      6.600000   2012.000000\n",
       "max    3.800000e+08  2.781506e+09   214.000000      8.100000   2015.000000"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe() # function to describe the dataset"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "DTIt7ezGVp-G"
   },
   "source": [
    "# Предобработка"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "jNb40DwKVp-H"
   },
   "outputs": [],
   "source": [
    "answers = {} # создадим словарь для ответов\n",
    "\n",
    "# тут другие ваши предобработки колонок например:\n",
    "data['profit'] = data['revenue'] - data['budget'] \n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "YxZaH-nPVp-L"
   },
   "source": [
    "# 1. У какого фильма из списка самый большой бюджет?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "Nd-G5gX6Vp-M"
   },
   "source": [
    "Использовать варианты ответов в коде решения запрещено.    \n",
    "Вы думаете и в жизни у вас будут варианты ответов?)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "uVnXAY5RVp-O"
   },
   "outputs": [],
   "source": [
    "answers['1'] = '723. Pirates of the Caribbean: On Stranger Tides (tt1298650)'# +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "723    Pirates of the Caribbean: On Stranger Tides\n",
       "Name: original_title, dtype: object"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data.budget == data.budget.max()]['original_title'] # to find the max budget film title "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "723    tt1298650\n",
       "Name: imdb_id, dtype: object"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data.budget == data.budget.max()]['imdb_id'] # to find the max budget film id "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "FNRbbI3vVp-c"
   },
   "source": [
    "# 2. Какой из фильмов самый длительный (в минутах)?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "vHAoEXNTVp-d"
   },
   "outputs": [],
   "source": [
    "answers['2'] = '1157. Gods and Generals (tt0279111)' # +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "ot-VX2XrVp-g"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1157    Gods and Generals\n",
       "Name: original_title, dtype: object"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data.runtime == data.runtime.max()]['original_title'] # to find the max runtime film title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1157    tt0279111\n",
       "Name: imdb_id, dtype: object"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data.runtime == data.runtime.max()]['imdb_id'] # to find the max runtime film id"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "bapLlpW8Vp-k"
   },
   "source": [
    "# 3. Какой из фильмов самый короткий (в минутах)?\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "YBxaSHuAVp-l"
   },
   "outputs": [],
   "source": [
    "answers['3'] = '768. Winnie the Pooh (tt1449283)' # +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "768    Winnie the Pooh\n",
       "Name: original_title, dtype: object"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data.runtime == data.runtime.min()]['original_title'] # to find the min runtime film title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "768    tt1449283\n",
       "Name: imdb_id, dtype: object"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data.runtime == data.runtime.min()]['imdb_id'] # to find the min runtime film id"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "TfQbxbfNVp-p"
   },
   "source": [
    "# 4. Какова средняя длительность фильмов?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['4'] = '110' # +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "109.6585494970884"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe().loc['mean', 'runtime'] # to find the mean runtime of films in the dataset"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "r5TvbnT_Vp-u"
   },
   "source": [
    "# 5. Каково медианное значение длительности фильмов? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "iBROplKnVp-v"
   },
   "outputs": [],
   "source": [
    "answers['5'] = '107' # +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "107.0"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe().loc['50%', 'runtime'] # to find the median runtime of films in the dataset (50% quantile)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "39P-deDSVp-y"
   },
   "source": [
    "# 6. Какой самый прибыльный фильм?\n",
    "#### Внимание! Здесь и далее под «прибылью» или «убытками» понимается разность между сборами и бюджетом фильма. (прибыль = сборы - бюджет) в нашем датасете это будет (profit = revenue - budget) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "UYZh4T9WVp-y"
   },
   "outputs": [],
   "source": [
    "answers['6'] = '239. Avatar (tt0499549)'# +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "239    Avatar\n",
       "Name: original_title, dtype: object"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data.profit == data.profit.max()]['original_title'] # to find the most profitable film title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "239    tt0499549\n",
       "Name: imdb_id, dtype: object"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data.profit == data.profit.max()]['imdb_id'] # to find the most profitable film id"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "M99JmIX4Vp-2"
   },
   "source": [
    "# 7. Какой фильм самый убыточный? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "w-D2m4XPVp-3"
   },
   "outputs": [],
   "source": [
    "answers['7'] = '1245. The Lone Ranger (tt1210819)'# +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1245    The Lone Ranger\n",
       "Name: original_title, dtype: object"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data.profit == data.profit.min()]['original_title'] # to find the most unprofitable film title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1245    tt1210819\n",
       "Name: imdb_id, dtype: object"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data.profit == data.profit.min()]['imdb_id'] # to find the most unprofitable film id"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "wEOM5ERVVp-6"
   },
   "source": [
    "# 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['8'] = '1478'# +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "y00_7HD6Vp-7"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1478"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(data[data.revenue > data.budget]) # to find the number of profitable films in the dataset"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "xhpspA9KVp_A"
   },
   "source": [
    "# 9. Какой фильм оказался самым кассовым в 2008 году?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['9'] = '599. The Dark Knight (tt0468569)'# +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "MoUyQr9RVp_B",
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "599                                      The Dark Knight\n",
       "603    Indiana Jones and the Kingdom of the Crystal S...\n",
       "606                                        Kung Fu Panda\n",
       "621                                              Hancock\n",
       "607                                           Mamma Mia!\n",
       "                             ...                        \n",
       "708                                   What Just Happened\n",
       "673                                        Transsiberian\n",
       "702                                   The Brothers Bloom\n",
       "711                              The Midnight Meat Train\n",
       "712                                    Mutant Chronicles\n",
       "Name: original_title, Length: 121, dtype: object"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# to find the most revenue film title in 2008\n",
    "data.loc[data.release_year.isin([2008])].sort_values(by = 'revenue', ascending = False)['original_title']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "599    tt0468569\n",
       "603    tt0367882\n",
       "606    tt0441773\n",
       "621    tt0448157\n",
       "607    tt0795421\n",
       "         ...    \n",
       "708    tt0486674\n",
       "673    tt0800241\n",
       "702    tt0844286\n",
       "711    tt0805570\n",
       "712    tt0490181\n",
       "Name: imdb_id, Length: 121, dtype: object"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# to find the most revenue film id in 2008\n",
    "data.loc[data.release_year.isin([2008])].sort_values(by = 'revenue', ascending = False)['imdb_id']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "Zi4hDKidVp_F"
   },
   "source": [
    "# 10. Самый убыточный фильм за период с 2012 по 2014 г. (включительно)?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['10'] = '1245. The Lone Ranger (tt1210819)'# +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "XqyRmufJVp_F",
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1245                    The Lone Ranger\n",
       "1214                           R.I.P.D.\n",
       "1007                        Upside Down\n",
       "1302    Legends of Oz: Dorothy's Return\n",
       "1235                 Bullet to the Head\n",
       "                     ...               \n",
       "1189                    Despicable Me 2\n",
       "974                             Skyfall\n",
       "1180                         Iron Man 3\n",
       "1177                             Frozen\n",
       "970                        The Avengers\n",
       "Name: original_title, Length: 367, dtype: object"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# to find the least revenue film title in period of 2012-2014\n",
    "data.loc[data.release_year.isin([2012, 2013, 2014])].sort_values(by = 'profit', ascending = True)['original_title']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1245    tt1210819\n",
       "1214    tt0790736\n",
       "1007    tt1374992\n",
       "1302    tt0884726\n",
       "1235    tt1308729\n",
       "          ...    \n",
       "1189    tt1690953\n",
       "974     tt1074638\n",
       "1180    tt1300854\n",
       "1177    tt2294629\n",
       "970     tt0848228\n",
       "Name: imdb_id, Length: 367, dtype: object"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# to find the least revenue film id in period of 2012-2014\n",
    "data.loc[data.release_year.isin([2012, 2013, 2014])].sort_values(by = 'profit', ascending = True)['imdb_id']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "EA7Sa9dkVp_I"
   },
   "source": [
    "# 11. Какого жанра фильмов больше всего?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "zsJAwJ8QVp_J"
   },
   "outputs": [],
   "source": [
    "answers['11'] = 'Drama'# -"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "otO3SbrSVp_N"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Drama'"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data11 = data.copy() # to copy dataset to avoid errors in the dataset\n",
    "data11['genres'] = data11.genres.str.split('|') # to split multiple kind of genres in the dataset in the only one \n",
    "data11= data11.explode('genres') # to add the only one genre in the every row in the dataset\n",
    "data11.genres.value_counts().index[0] # to count every kind of genres and display the most"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "T9_bPWpkVp_Q"
   },
   "source": [
    "# 12. Фильмы какого жанра чаще всего становятся прибыльными? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['12'] = 'Drama'# +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "Tmt8MaK1Vp_R"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Drama'"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_12 = data.copy() # to copy dataset to avoid errors in the dataset\n",
    "data12 = data_12.query('revenue > budget').copy() # to find all profitable films in the dataset\n",
    "data12['genres'] = data12.genres.str.split('|') # to split multiple kind of genres in the dataset in the only one\n",
    "data12=data12.explode('genres') # to add the only one genre in the every row in the dataset\n",
    "profit_genre = data12.genres.value_counts().index[0] # to count every kind of genres and display the most\n",
    "profit_genre"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "0F23bgsDVp_U"
   },
   "source": [
    "# 13. У какого режиссера самые большие суммарные кассовые сборы?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['13'] = 'Peter Jackson' # +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "K6Z3J8ygVp_X"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Peter Jackson'"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data13=data.copy() # to copy dataset to avoid errors in the dataset\n",
    "data13['director'] = data13.director.str.split('|') # to split multiple kind of directors in the dataset in the only one \n",
    "data13=data13.explode('director') # to add the only one director in the every row in the dataset\n",
    "# to group dataset by \"director's\" and \" sum revenue's\" data and display the most sum film revenue name director\n",
    "data13.groupby(['director'])['revenue'].sum().sort_values(ascending=False).index[0] "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "PsYC9FgRVp_a"
   },
   "source": [
    "# 14. Какой режисер снял больше всего фильмов в стиле Action?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['14'] = 'Robert Rodriguez' # +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "wd2M-wHeVp_b",
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Robert Rodriguez'"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data14 = data[data.genres.str.contains('Action')].copy() # to copy dataset contains \"Action\" genre \n",
    "data14.director = data14.director.str.split('|') # to split multiple kind of directors in the dataset in the only one \n",
    "data14 = data14.explode('director') # to add the only one director in the every row in the dataset \n",
    "# to count every name of directors and display the most \"Action\" productive name director\n",
    "data14.director.value_counts().index[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "PQ0KciD7Vp_f"
   },
   "source": [
    "# 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['15'] = 'Chris Hemsworth' # +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'data15' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-40-36be8d0dbd1e>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# to copy dataset contains revenue in 2012\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mdata15\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdata15\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mloc\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mdata15\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrelease_year\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0misin\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m2012\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msort_values\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mby\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'revenue'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mascending\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcopy\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mdata15\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcast\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdata15\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcast\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mstr\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'|'\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;31m# to split multiple kind of actors in the dataset in the only one\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mdata15\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdata15\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexplode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'cast'\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;31m# to add the only one actor in the every row in the dataset\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;31m# to group dataset by \"actor\" and \" sum revenue\" data and display the most sum film revenue name actor\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'data15' is not defined"
     ]
    }
   ],
   "source": [
    "# to copy dataset contains revenue in 2012\n",
    "data15 = data15.loc[data15.release_year.isin([2012])].sort_values(by = 'revenue', ascending = True).copy()\n",
    "data15.cast = data15.cast.str.split('|') # to split multiple kind of actors in the dataset in the only one \n",
    "data15 = data15.explode('cast') # to add the only one actor in the every row in the dataset \n",
    "# to group dataset by \"actor\" and \" sum revenue\" data and display the most sum film revenue name actor\n",
    "data15.groupby('cast').revenue.sum().idxmax()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "mWHyyL7QVp_j"
   },
   "source": [
    "# 16. Какой актер снялся в большем количестве высокобюджетных фильмов?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['16'] = 'Matt Damon' # +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "qQtmHKTFVp_k"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Matt Damon'"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data16 = data.copy() # to copy dataset to avoid errors in the dataset\n",
    "data16 = data16.query('budget > budget.mean()') # to find the all high-budget films in the dataset\n",
    "data16['cast'] = data16.cast.str.split('|') # to split multiple kind of actors in the dataset in the only one \n",
    "data16=data16.explode('cast') # to add the only one actor in the every row in the dataset    \n",
    "# to count every name of actors and display the most high-budget film name actor\n",
    "data16.cast.value_counts().index[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "NIh6AaW5Vp_n"
   },
   "source": [
    "# 17. В фильмах какого жанра больше всего снимался Nicolas Cage? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['17'] = 'Action' # +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "H74SJDIBVp_n"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Action'"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data17 = data.copy() # to copy dataset to avoid errors in the dataset\n",
    "data17 = data17[data17.cast.str.contains('Nicolas Cage')] # to find all films with Nicolas Cage in the dataset\n",
    "data17.genres = data17.genres.str.split('|')  # to split multiple kind of genres in the dataset in the only one\n",
    "data17 = data17.explode('genres') # to add the only one genre in the every row in the dataset\n",
    "data17.genres.value_counts().index[0] # to count every kind of genres and display the most frequently encountered"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "RqOmPRfWVp_q"
   },
   "source": [
    "# 18. Самый убыточный фильм от Paramount Pictures"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['18'] = 'K-19: The Widowmaker' # +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "9E_B0Y96Vp_r"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'K-19: The Widowmaker'"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data18 = data.copy()  # to copy dataset to avoid errors in the dataset\n",
    "# to find all Paramount Pictures films in the dataset\n",
    "data18 = data18[data18.production_companies.str.contains('Paramount Pictures')] \n",
    "# to group dataset by \"original_title\" and \" profit\" data and display the the most unprofitable film\n",
    "data18.groupby(['original_title'])['profit'].min().sort_values(ascending=True).index[0] "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "vS8Ur6ddVp_u"
   },
   "source": [
    "# 19. Какой год стал самым успешным по суммарным кассовым сборам?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['19'] = '2015' # +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "Dnbt4GdIVp_v"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2015"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data19 = data.copy() # to copy dataset to avoid errors in the dataset\n",
    "# to group dataset by \"release_year\" and \"sum revenue\" data and display the the most revenue year\n",
    "data19.groupby(['release_year'])['revenue'].sum().sort_values(ascending=False).index[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "JAzJh4QAVp_z"
   },
   "source": [
    "# 20. Какой самый прибыльный год для студии Warner Bros?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['20'] = '2011' # +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "wgVu02DEVp_0"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2011"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data20 = data.copy() # to copy dataset to avoid errors in the dataset\n",
    "# to find all Warner Bros films in the dataset\n",
    "data20 = data20[data20.production_companies.str.contains('Warner Bros')]\n",
    "# to group dataset by \"release_year\" and \"profit\" data and display the most profitable year\n",
    "data20.groupby(['release_year'])['profit'].max().sort_values(ascending=False).index[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "8Im1S2HRVp_4"
   },
   "source": [
    "# 21. В каком месяце за все годы суммарно вышло больше всего фильмов?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['21'] = 'September' # +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "lev6TH7gVp_4"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "В январе за отчетный период суммарно выпущено -  110 фильмов\n",
      "В июне за отчетный период суммарно выпущено -  147 фильмов\n",
      "В декабре за отчетный период суммарно выпущено -  190 фильмов\n",
      "В сентябре за отчетный период суммарно выпущено -  227 фильмов\n",
      "В мае за отчетный период суммарно выпущено -  140 фильмов\n"
     ]
    }
   ],
   "source": [
    "data21 = data.copy() # to copy dataset to avoid errors in the dataset\n",
    "data21.release_date = data.release_date.apply(lambda x: dt.datetime.strptime(x, '%m/%d/%Y')) # to set date format\n",
    "data21.release_date = data21.release_date.apply(lambda x: x.strftime('%B')) # to left only name's month's\n",
    "num1 = data21.query('release_date in [\"January\"]').shape[0] # to find the film number in January\n",
    "num2 = data21.query('release_date in [\"June\"]').shape[0] # to find the film number in June\n",
    "num3 = data21.query('release_date in [\"December\"]').shape[0] # to find the film number in December\n",
    "num4 = data21.query('release_date in [\"September\"]').shape[0] # to find the film number in September\n",
    "num5 = data21.query('release_date in [\"May\"]').shape[0] # to find the film number in May\n",
    "print('В январе за отчетный период суммарно выпущено - ', num1, 'фильмов')\n",
    "print('В июне за отчетный период суммарно выпущено - ', num2, 'фильмов')\n",
    "print('В декабре за отчетный период суммарно выпущено - ', num3, 'фильмов')\n",
    "print('В сентябре за отчетный период суммарно выпущено - ', num4, 'фильмов')\n",
    "print('В мае за отчетный период суммарно выпущено - ', num5, 'фильмов')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "uAJsZ_NeVp_7"
   },
   "source": [
    "# 22. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['22'] = '450' # +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "Aa-hEREoVp_8"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "450"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data22 = data.copy() # to copy dataset to avoid errors in the dataset\n",
    "data22['release_date'] = pd.to_datetime(data22['release_date']) # to set date format\n",
    "data22.release_date = data22.release_date.apply(lambda x: x.strftime('%B')) # to left only name's month's\n",
    "data22.query('release_date in [\"June\", \"July\", \"August\"]').shape[0] # to find the film number in June, July, August"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "G94ppOY1VqAA"
   },
   "source": [
    "# 23. Для какого режиссера зима – самое продуктивное время года? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['23'] = 'Peter Jackson' # +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "RhNTsamuVqAB"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Peter Jackson'"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_23 = data.copy() # to copy dataset to avoid errors in the dataset\n",
    "data_23.release_date = data.release_date.apply(lambda x: dt.datetime.strptime(x, '%m/%d/%Y')) # to set date format\n",
    "data_23.release_date = data_23.release_date.apply(lambda x: x.strftime('%B')) # to left only name's month's\n",
    "# to find all films in December, January, February\n",
    "data_23 = data_23.query('release_date in [\"December\", \"January\", \"February\"]') \n",
    "data_23['director'] = data_23.director.str.split('|') # to split multiple kind of directors in the dataset in the only one \n",
    "data_23 = data_23.explode('director') # to add the only one director in the every row in the dataset \n",
    "# to group dataset by \"director\" and \"imdb_id\" data and display the most productive name director in winter's month's\n",
    "data_23.groupby(['director'])['imdb_id'].count().sort_values(ascending = False).index[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "RBo0JVjVVqAF"
   },
   "source": [
    "# 24. Какая студия дает самые длинные названия своим фильмам по количеству символов?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['24'] = 'Four By Two Productions' # +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "QRGS8L0iVqAG"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Four By Two Productions'"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data24 = data.copy() # to copy dataset to avoid errors in the dataset\n",
    "# to split multiple kind of production companies in the dataset in the only one \n",
    "data24['production_companies'] = data24.production_companies.str.split('|') \n",
    "data24 = data24.explode('production_companies') # to add the only one name of production company in the every row in the dataset \n",
    "data24['title_len'] = data24['original_title'].apply(len) # to find all titles length\n",
    "# to group dataset by \"production_companies\" and \"title_len\" data and display the production company with the most title length films\n",
    "data24.groupby('production_companies').title_len.mean().sort_values(ascending = False).index[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "9G0hbvR7VqAK"
   },
   "source": [
    "# 25. Описание фильмов какой студии в среднем самые длинные по количеству слов?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['25'] = 'Midnight Picture Show' # +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "Ge2GsLNxVqAK"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Midnight Picture Show'"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data25 = data.copy() # to copy dataset to avoid errors in the dataset\n",
    "# to split multiple kind of production companies in the dataset in the only one \n",
    "data25['production_companies'] = data25.production_companies.str.split('|')\n",
    "data25 = data25.explode('production_companies') # to add the only one name of production company in the every row in the dataset \n",
    "def len_words(s): # to call the len_word function\n",
    "    return len(s.split(' ')) # to split using ' '\n",
    "# to create the pivot table and find the production company with the most overview length films\n",
    "data25['overview_len'] = data25.overview.apply(len_words)  \n",
    "data25.pivot_table(['overview_len'],['production_companies'], \n",
    "                   aggfunc='mean').sort_values(by='overview_len',                                              \n",
    "                                            ascending = False).index[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "FJ1AFt90VqAP"
   },
   "source": [
    "# 26. Какие фильмы входят в 1 процент лучших по рейтингу? \n",
    "по vote_average"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['26'] = 'Inside Out, The Dark Knight, 12 Years a Slave' # +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "8qmJVq4CVqAQ",
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>imdb_id</th>\n",
       "      <th>budget</th>\n",
       "      <th>revenue</th>\n",
       "      <th>original_title</th>\n",
       "      <th>cast</th>\n",
       "      <th>director</th>\n",
       "      <th>tagline</th>\n",
       "      <th>overview</th>\n",
       "      <th>runtime</th>\n",
       "      <th>genres</th>\n",
       "      <th>production_companies</th>\n",
       "      <th>release_date</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>release_year</th>\n",
       "      <th>profit</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>tt2096673</td>\n",
       "      <td>175000000</td>\n",
       "      <td>853708609</td>\n",
       "      <td>Inside Out</td>\n",
       "      <td>Amy Poehler|Phyllis Smith|Richard Kind|Bill Ha...</td>\n",
       "      <td>Pete Docter</td>\n",
       "      <td>Meet the little voices inside your head.</td>\n",
       "      <td>Growing up can be a bumpy road, and it's no ex...</td>\n",
       "      <td>94</td>\n",
       "      <td>Comedy|Animation|Family</td>\n",
       "      <td>Walt Disney Pictures|Pixar Animation Studios|W...</td>\n",
       "      <td>6/9/2015</td>\n",
       "      <td>8.0</td>\n",
       "      <td>2015</td>\n",
       "      <td>678708609</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>34</th>\n",
       "      <td>tt3170832</td>\n",
       "      <td>6000000</td>\n",
       "      <td>35401758</td>\n",
       "      <td>Room</td>\n",
       "      <td>Brie Larson|Jacob Tremblay|Joan Allen|Sean Bri...</td>\n",
       "      <td>Lenny Abrahamson</td>\n",
       "      <td>Love knows no boundaries</td>\n",
       "      <td>Jack is a young boy of 5 years old who has liv...</td>\n",
       "      <td>117</td>\n",
       "      <td>Drama|Thriller</td>\n",
       "      <td>Element Pictures|No Trace Camping|A24|Duperele...</td>\n",
       "      <td>10/16/2015</td>\n",
       "      <td>8.0</td>\n",
       "      <td>2015</td>\n",
       "      <td>29401758</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>118</th>\n",
       "      <td>tt0816692</td>\n",
       "      <td>165000000</td>\n",
       "      <td>621752480</td>\n",
       "      <td>Interstellar</td>\n",
       "      <td>Matthew McConaughey|Jessica Chastain|Anne Hath...</td>\n",
       "      <td>Christopher Nolan</td>\n",
       "      <td>Mankind was born on Earth. It was never meant ...</td>\n",
       "      <td>Interstellar chronicles the adventures of a gr...</td>\n",
       "      <td>169</td>\n",
       "      <td>Adventure|Drama|Science Fiction</td>\n",
       "      <td>Paramount Pictures|Legendary Pictures|Warner B...</td>\n",
       "      <td>11/5/2014</td>\n",
       "      <td>8.0</td>\n",
       "      <td>2014</td>\n",
       "      <td>456752480</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>119</th>\n",
       "      <td>tt2015381</td>\n",
       "      <td>170000000</td>\n",
       "      <td>773312399</td>\n",
       "      <td>Guardians of the Galaxy</td>\n",
       "      <td>Chris Pratt|Zoe Saldana|Dave Bautista|Vin Dies...</td>\n",
       "      <td>James Gunn</td>\n",
       "      <td>All heroes start somewhere.</td>\n",
       "      <td>Light years from Earth, 26 years after being a...</td>\n",
       "      <td>121</td>\n",
       "      <td>Action|Science Fiction|Adventure</td>\n",
       "      <td>Marvel Studios|Moving Picture Company (MPC)|Bu...</td>\n",
       "      <td>7/30/2014</td>\n",
       "      <td>7.9</td>\n",
       "      <td>2014</td>\n",
       "      <td>603312399</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>125</th>\n",
       "      <td>tt2084970</td>\n",
       "      <td>14000000</td>\n",
       "      <td>233555708</td>\n",
       "      <td>The Imitation Game</td>\n",
       "      <td>Benedict Cumberbatch|Keira Knightley|Matthew G...</td>\n",
       "      <td>Morten Tyldum</td>\n",
       "      <td>The true enigma was the man who cracked the code.</td>\n",
       "      <td>Based on the real life story of legendary cryp...</td>\n",
       "      <td>113</td>\n",
       "      <td>History|Drama|Thriller|War</td>\n",
       "      <td>Black Bear Pictures|Bristol Automotive</td>\n",
       "      <td>11/14/2014</td>\n",
       "      <td>8.0</td>\n",
       "      <td>2014</td>\n",
       "      <td>219555708</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>128</th>\n",
       "      <td>tt2267998</td>\n",
       "      <td>61000000</td>\n",
       "      <td>369330363</td>\n",
       "      <td>Gone Girl</td>\n",
       "      <td>Ben Affleck|Rosamund Pike|Carrie Coon|Neil Pat...</td>\n",
       "      <td>David Fincher</td>\n",
       "      <td>You don't know what you've got 'til it's...</td>\n",
       "      <td>With his wife's disappearance having become th...</td>\n",
       "      <td>145</td>\n",
       "      <td>Mystery|Thriller|Drama</td>\n",
       "      <td>Twentieth Century Fox Film Corporation|Regency...</td>\n",
       "      <td>10/1/2014</td>\n",
       "      <td>7.9</td>\n",
       "      <td>2014</td>\n",
       "      <td>308330363</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>138</th>\n",
       "      <td>tt2278388</td>\n",
       "      <td>30000000</td>\n",
       "      <td>174600318</td>\n",
       "      <td>The Grand Budapest Hotel</td>\n",
       "      <td>Ralph Fiennes|Tony Revolori|F. Murray Abraham|...</td>\n",
       "      <td>Wes Anderson</td>\n",
       "      <td>A perfect holiday without leaving home.</td>\n",
       "      <td>The Grand Budapest Hotel tells of a legendary ...</td>\n",
       "      <td>99</td>\n",
       "      <td>Comedy|Drama</td>\n",
       "      <td>Fox Searchlight Pictures|Scott Rudin Productio...</td>\n",
       "      <td>2/26/2014</td>\n",
       "      <td>7.9</td>\n",
       "      <td>2014</td>\n",
       "      <td>144600318</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>370</th>\n",
       "      <td>tt1375666</td>\n",
       "      <td>160000000</td>\n",
       "      <td>825500000</td>\n",
       "      <td>Inception</td>\n",
       "      <td>Leonardo DiCaprio|Joseph Gordon-Levitt|Ellen P...</td>\n",
       "      <td>Christopher Nolan</td>\n",
       "      <td>Your mind is the scene of the crime.</td>\n",
       "      <td>Cobb, a skilled thief who commits corporate es...</td>\n",
       "      <td>148</td>\n",
       "      <td>Action|Thriller|Science Fiction|Mystery|Adventure</td>\n",
       "      <td>Legendary Pictures|Warner Bros.|Syncopy</td>\n",
       "      <td>7/14/2010</td>\n",
       "      <td>7.9</td>\n",
       "      <td>2010</td>\n",
       "      <td>665500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>599</th>\n",
       "      <td>tt0468569</td>\n",
       "      <td>185000000</td>\n",
       "      <td>1001921825</td>\n",
       "      <td>The Dark Knight</td>\n",
       "      <td>Christian Bale|Michael Caine|Heath Ledger|Aaro...</td>\n",
       "      <td>Christopher Nolan</td>\n",
       "      <td>Why So Serious?</td>\n",
       "      <td>Batman raises the stakes in his war on crime. ...</td>\n",
       "      <td>152</td>\n",
       "      <td>Drama|Action|Crime|Thriller</td>\n",
       "      <td>DC Comics|Legendary Pictures|Warner Bros.|Syncopy</td>\n",
       "      <td>7/16/2008</td>\n",
       "      <td>8.1</td>\n",
       "      <td>2008</td>\n",
       "      <td>816921825</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>872</th>\n",
       "      <td>tt0253474</td>\n",
       "      <td>35000000</td>\n",
       "      <td>120072577</td>\n",
       "      <td>The Pianist</td>\n",
       "      <td>Adrien Brody|Thomas Kretschmann|Frank Finlay|M...</td>\n",
       "      <td>Roman Polanski</td>\n",
       "      <td>Music was his passion. Survival was his master...</td>\n",
       "      <td>The Pianist is a film adapted from the biograp...</td>\n",
       "      <td>150</td>\n",
       "      <td>Drama|War</td>\n",
       "      <td>Bac Films|Canal+Polska|Heritage Films|Studio B...</td>\n",
       "      <td>9/24/2002</td>\n",
       "      <td>7.9</td>\n",
       "      <td>2002</td>\n",
       "      <td>85072577</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1081</th>\n",
       "      <td>tt0167260</td>\n",
       "      <td>94000000</td>\n",
       "      <td>1118888979</td>\n",
       "      <td>The Lord of the Rings: The Return of the King</td>\n",
       "      <td>Elijah Wood|Ian McKellen|Viggo Mortensen|Liv T...</td>\n",
       "      <td>Peter Jackson</td>\n",
       "      <td>The eye of the enemy is moving.</td>\n",
       "      <td>Aragorn is revealed as the heir to the ancient...</td>\n",
       "      <td>201</td>\n",
       "      <td>Adventure|Fantasy|Action</td>\n",
       "      <td>WingNut Films|New Line Cinema</td>\n",
       "      <td>12/1/2003</td>\n",
       "      <td>7.9</td>\n",
       "      <td>2003</td>\n",
       "      <td>1024888979</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1183</th>\n",
       "      <td>tt0993846</td>\n",
       "      <td>100000000</td>\n",
       "      <td>392000694</td>\n",
       "      <td>The Wolf of Wall Street</td>\n",
       "      <td>Leonardo DiCaprio|Jonah Hill|Margot Robbie|Kyl...</td>\n",
       "      <td>Martin Scorsese</td>\n",
       "      <td>EARN. SPEND. PARTY.</td>\n",
       "      <td>A New York stockbroker refuses to cooperate in...</td>\n",
       "      <td>180</td>\n",
       "      <td>Crime|Drama|Comedy</td>\n",
       "      <td>Paramount Pictures|Appian Way|EMJAG Production...</td>\n",
       "      <td>12/25/2013</td>\n",
       "      <td>7.9</td>\n",
       "      <td>2013</td>\n",
       "      <td>292000694</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1191</th>\n",
       "      <td>tt2024544</td>\n",
       "      <td>20000000</td>\n",
       "      <td>187000000</td>\n",
       "      <td>12 Years a Slave</td>\n",
       "      <td>Chiwetel Ejiofor|Michael Fassbender|Lupita Nyo...</td>\n",
       "      <td>Steve McQueen</td>\n",
       "      <td>The extraordinary true story of Solomon Northup</td>\n",
       "      <td>In the pre-Civil War United States, Solomon No...</td>\n",
       "      <td>134</td>\n",
       "      <td>Drama|History</td>\n",
       "      <td>Plan B Entertainment|Regency Enterprises|River...</td>\n",
       "      <td>10/18/2013</td>\n",
       "      <td>7.9</td>\n",
       "      <td>2013</td>\n",
       "      <td>167000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1800</th>\n",
       "      <td>tt0209144</td>\n",
       "      <td>9000000</td>\n",
       "      <td>39723096</td>\n",
       "      <td>Memento</td>\n",
       "      <td>Guy Pearce|Carrie-Anne Moss|Joe Pantoliano|Mar...</td>\n",
       "      <td>Christopher Nolan</td>\n",
       "      <td>Some memories are best forgotten.</td>\n",
       "      <td>Suffering short-term memory loss after a head ...</td>\n",
       "      <td>113</td>\n",
       "      <td>Mystery|Thriller</td>\n",
       "      <td>Summit Entertainment|Newmarket Capital Group|T...</td>\n",
       "      <td>10/11/2000</td>\n",
       "      <td>7.9</td>\n",
       "      <td>2000</td>\n",
       "      <td>30723096</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        imdb_id     budget     revenue  \\\n",
       "9     tt2096673  175000000   853708609   \n",
       "34    tt3170832    6000000    35401758   \n",
       "118   tt0816692  165000000   621752480   \n",
       "119   tt2015381  170000000   773312399   \n",
       "125   tt2084970   14000000   233555708   \n",
       "128   tt2267998   61000000   369330363   \n",
       "138   tt2278388   30000000   174600318   \n",
       "370   tt1375666  160000000   825500000   \n",
       "599   tt0468569  185000000  1001921825   \n",
       "872   tt0253474   35000000   120072577   \n",
       "1081  tt0167260   94000000  1118888979   \n",
       "1183  tt0993846  100000000   392000694   \n",
       "1191  tt2024544   20000000   187000000   \n",
       "1800  tt0209144    9000000    39723096   \n",
       "\n",
       "                                     original_title  \\\n",
       "9                                        Inside Out   \n",
       "34                                             Room   \n",
       "118                                    Interstellar   \n",
       "119                         Guardians of the Galaxy   \n",
       "125                              The Imitation Game   \n",
       "128                                       Gone Girl   \n",
       "138                        The Grand Budapest Hotel   \n",
       "370                                       Inception   \n",
       "599                                 The Dark Knight   \n",
       "872                                     The Pianist   \n",
       "1081  The Lord of the Rings: The Return of the King   \n",
       "1183                        The Wolf of Wall Street   \n",
       "1191                               12 Years a Slave   \n",
       "1800                                        Memento   \n",
       "\n",
       "                                                   cast           director  \\\n",
       "9     Amy Poehler|Phyllis Smith|Richard Kind|Bill Ha...        Pete Docter   \n",
       "34    Brie Larson|Jacob Tremblay|Joan Allen|Sean Bri...   Lenny Abrahamson   \n",
       "118   Matthew McConaughey|Jessica Chastain|Anne Hath...  Christopher Nolan   \n",
       "119   Chris Pratt|Zoe Saldana|Dave Bautista|Vin Dies...         James Gunn   \n",
       "125   Benedict Cumberbatch|Keira Knightley|Matthew G...      Morten Tyldum   \n",
       "128   Ben Affleck|Rosamund Pike|Carrie Coon|Neil Pat...      David Fincher   \n",
       "138   Ralph Fiennes|Tony Revolori|F. Murray Abraham|...       Wes Anderson   \n",
       "370   Leonardo DiCaprio|Joseph Gordon-Levitt|Ellen P...  Christopher Nolan   \n",
       "599   Christian Bale|Michael Caine|Heath Ledger|Aaro...  Christopher Nolan   \n",
       "872   Adrien Brody|Thomas Kretschmann|Frank Finlay|M...     Roman Polanski   \n",
       "1081  Elijah Wood|Ian McKellen|Viggo Mortensen|Liv T...      Peter Jackson   \n",
       "1183  Leonardo DiCaprio|Jonah Hill|Margot Robbie|Kyl...    Martin Scorsese   \n",
       "1191  Chiwetel Ejiofor|Michael Fassbender|Lupita Nyo...      Steve McQueen   \n",
       "1800  Guy Pearce|Carrie-Anne Moss|Joe Pantoliano|Mar...  Christopher Nolan   \n",
       "\n",
       "                                                tagline  \\\n",
       "9              Meet the little voices inside your head.   \n",
       "34                             Love knows no boundaries   \n",
       "118   Mankind was born on Earth. It was never meant ...   \n",
       "119                         All heroes start somewhere.   \n",
       "125   The true enigma was the man who cracked the code.   \n",
       "128         You don't know what you've got 'til it's...   \n",
       "138             A perfect holiday without leaving home.   \n",
       "370                Your mind is the scene of the crime.   \n",
       "599                                     Why So Serious?   \n",
       "872   Music was his passion. Survival was his master...   \n",
       "1081                    The eye of the enemy is moving.   \n",
       "1183                                EARN. SPEND. PARTY.   \n",
       "1191    The extraordinary true story of Solomon Northup   \n",
       "1800                  Some memories are best forgotten.   \n",
       "\n",
       "                                               overview  runtime  \\\n",
       "9     Growing up can be a bumpy road, and it's no ex...       94   \n",
       "34    Jack is a young boy of 5 years old who has liv...      117   \n",
       "118   Interstellar chronicles the adventures of a gr...      169   \n",
       "119   Light years from Earth, 26 years after being a...      121   \n",
       "125   Based on the real life story of legendary cryp...      113   \n",
       "128   With his wife's disappearance having become th...      145   \n",
       "138   The Grand Budapest Hotel tells of a legendary ...       99   \n",
       "370   Cobb, a skilled thief who commits corporate es...      148   \n",
       "599   Batman raises the stakes in his war on crime. ...      152   \n",
       "872   The Pianist is a film adapted from the biograp...      150   \n",
       "1081  Aragorn is revealed as the heir to the ancient...      201   \n",
       "1183  A New York stockbroker refuses to cooperate in...      180   \n",
       "1191  In the pre-Civil War United States, Solomon No...      134   \n",
       "1800  Suffering short-term memory loss after a head ...      113   \n",
       "\n",
       "                                                 genres  \\\n",
       "9                               Comedy|Animation|Family   \n",
       "34                                       Drama|Thriller   \n",
       "118                     Adventure|Drama|Science Fiction   \n",
       "119                    Action|Science Fiction|Adventure   \n",
       "125                          History|Drama|Thriller|War   \n",
       "128                              Mystery|Thriller|Drama   \n",
       "138                                        Comedy|Drama   \n",
       "370   Action|Thriller|Science Fiction|Mystery|Adventure   \n",
       "599                         Drama|Action|Crime|Thriller   \n",
       "872                                           Drama|War   \n",
       "1081                           Adventure|Fantasy|Action   \n",
       "1183                                 Crime|Drama|Comedy   \n",
       "1191                                      Drama|History   \n",
       "1800                                   Mystery|Thriller   \n",
       "\n",
       "                                   production_companies release_date  \\\n",
       "9     Walt Disney Pictures|Pixar Animation Studios|W...     6/9/2015   \n",
       "34    Element Pictures|No Trace Camping|A24|Duperele...   10/16/2015   \n",
       "118   Paramount Pictures|Legendary Pictures|Warner B...    11/5/2014   \n",
       "119   Marvel Studios|Moving Picture Company (MPC)|Bu...    7/30/2014   \n",
       "125              Black Bear Pictures|Bristol Automotive   11/14/2014   \n",
       "128   Twentieth Century Fox Film Corporation|Regency...    10/1/2014   \n",
       "138   Fox Searchlight Pictures|Scott Rudin Productio...    2/26/2014   \n",
       "370             Legendary Pictures|Warner Bros.|Syncopy    7/14/2010   \n",
       "599   DC Comics|Legendary Pictures|Warner Bros.|Syncopy    7/16/2008   \n",
       "872   Bac Films|Canal+Polska|Heritage Films|Studio B...    9/24/2002   \n",
       "1081                      WingNut Films|New Line Cinema    12/1/2003   \n",
       "1183  Paramount Pictures|Appian Way|EMJAG Production...   12/25/2013   \n",
       "1191  Plan B Entertainment|Regency Enterprises|River...   10/18/2013   \n",
       "1800  Summit Entertainment|Newmarket Capital Group|T...   10/11/2000   \n",
       "\n",
       "      vote_average  release_year      profit  \n",
       "9              8.0          2015   678708609  \n",
       "34             8.0          2015    29401758  \n",
       "118            8.0          2014   456752480  \n",
       "119            7.9          2014   603312399  \n",
       "125            8.0          2014   219555708  \n",
       "128            7.9          2014   308330363  \n",
       "138            7.9          2014   144600318  \n",
       "370            7.9          2010   665500000  \n",
       "599            8.1          2008   816921825  \n",
       "872            7.9          2002    85072577  \n",
       "1081           7.9          2003  1024888979  \n",
       "1183           7.9          2013   292000694  \n",
       "1191           7.9          2013   167000000  \n",
       "1800           7.9          2000    30723096  "
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data26 = data.copy() # to copy dataset to avoid errors in the dataset\n",
    "# to find the best 1% vote average films using 99% quantile\n",
    "data26[data26['vote_average'] > data26['vote_average'].quantile(q=0.99)] "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "MdXsUXbCVqAV"
   },
   "source": [
    "# 27. Какие актеры чаще всего снимаются в одном фильме вместе?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [],
   "source": [
    "answers['27'] = 'Daniel Radcliffe, Rupert Grint' # +"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(Daniel Radcliffe, Emma Watson)              8\n",
       "(Daniel Radcliffe, Rupert Grint)             8\n",
       "(Rupert Grint, Emma Watson)                  7\n",
       "(Johnny Depp, Helena Bonham Carter)          6\n",
       "(Ben Stiller, Owen Wilson)                   6\n",
       "                                            ..\n",
       "(Maggie Grace, Katie Cassidy)                1\n",
       "(Jennifer Aniston, Kevin Spacey)             1\n",
       "(Arnold Schwarzenegger, Michael Rapaport)    1\n",
       "(Rinko Kikuchi, Robbie Coltrane)             1\n",
       "(Kristen Wilson, Raven-SymonÃ©)              1\n",
       "Name: cast, Length: 18121, dtype: int64"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data27 = data.copy() # to copy dataset to avoid errors in the dataset\n",
    "# to split multiple kind of name actors in the dataset in the two \n",
    "data27['cast'] = data27.cast.str.split('|').apply(lambda x: list(itertools.combinations(x, 2)))\n",
    "data27_1 = data27.explode('cast') # to add two names of actors in the every row in the dataset  \n",
    "data27_1.cast.value_counts() # to count"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "U0nONFnGVqAX"
   },
   "source": [
    "# Submission"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "IfcaRO9-VqAX",
    "outputId": "0f132912-32bb-4196-c98c-abfbc4ad5a5f"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'1': '723. Pirates of the Caribbean: On Stranger Tides (tt1298650)',\n",
       " '2': '1157. Gods and Generals (tt0279111)',\n",
       " '3': '768. Winnie the Pooh (tt1449283)',\n",
       " '4': '110',\n",
       " '5': '107',\n",
       " '6': '239. Avatar (tt0499549)',\n",
       " '7': '1245. The Lone Ranger (tt1210819)',\n",
       " '8': '1478',\n",
       " '9': '599. The Dark Knight (tt0468569)',\n",
       " '10': '1245. The Lone Ranger (tt1210819)',\n",
       " '11': 'Drama',\n",
       " '12': 'Drama',\n",
       " '13': 'Peter Jackson',\n",
       " '14': 'Robert Rodriguez',\n",
       " '15': 'Chris Hemsworth',\n",
       " '18': 'K-19: The Widowmaker',\n",
       " '19': '2015',\n",
       " '20': '2011',\n",
       " '21': 'September',\n",
       " '22': '450',\n",
       " '23': 'Peter Jackson',\n",
       " '24': 'Four By Two Productions',\n",
       " '25': 'Midnight Picture Show',\n",
       " '26': 'Inside Out, The Dark Knight, 12 Years a Slave',\n",
       " '27': 'Daniel Radcliffe, Rupert Grint',\n",
       " '16': 'Matt Damon',\n",
       " '17': 'Action'}"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "answers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "SiRmHPl8VqAd"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "27"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(answers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "colab": {
   "name": "Copy of [SF-DST] Movies IMBD v4.1 TEMPLATE.ipynb",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
