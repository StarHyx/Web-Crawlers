import expanddouban
import csv

from bs4 import BeautifulSoup

# my favorite three categories of movies
category_list = ["战争", "喜剧", "科幻"]
location_list = ["大陆", "美国", "香港", "台湾", "日本", "韩国", "英国", "法国", "德国", "意大利", "西班牙", "印度", "泰国", "俄罗斯", "伊朗", "加拿大", "澳大利亚", "爱尔兰", "瑞典", "巴西", "丹麦"]

"""
return a string corresponding to the URL of douban movie lists given category and location.
"""
def getMovieUrl(category, location):
    url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,{},{}".format(category, location)
    return url

"""
return a list of Movie objects with the given category and location.
"""
def getMovies(category, location):

    # get the content of html using bs4
    url = getMovieUrl(category,location)
    html = expanddouban.getHtml(url)
    soup = BeautifulSoup(html, "html.parser")

    # lists using for store the information of the movies
    movie_name_list = []
    movie_rate_list = []
    movie_info_link_list = []
    movie_cover_link_list = []
    movie_numbers = 0
    movie_list = []

    # crawling needed information
    movie_content = soup.find(id="content").find(class_="list-wp")

    for movie in movie_content.find_all('a'):
        movie_name_list.append(movie.find('span', class_="title").get_text())
        movie_rate_list.append(movie.find('span', class_="rate").get_text())
        movie_info_link_list.append(movie.get('href'))
        movie_cover_link_list.append(movie.find('img').get('src'))
        movie_numbers += 1


    # the sturctur of movie : movie(name, rate, location, category, info_link, cover_link)
    for i in range(movie_numbers):
        list = [movie_name_list[i],movie_rate_list[i],location,category,movie_info_link_list[i],movie_cover_link_list[i]]
        movie_list.append(list)

    # return the movie list, each elements in it is a list with the structure of movie
    return movie_list

"""
count the locations with top three movie numbers for each category, and write the result into a txt file.
"""
def dataStatistics(category, movie_elements):
    sorted_list = sorted(movie_numbers_dict.items(), key=lambda item:item[1], reverse = True)
    # Aftering sorting the dictionary by the value, it will return a list
    # The first element will be the total number of movies in this catelog
    # And the next three elements will contain the informantin of the top three locations and their movie numbers
    # That's what we need to write in the output file.

    total_movie_number = sorted_list[0][1]

    first_location = sorted_list[1][0]
    second_location = sorted_list[2][0]
    third_location = sorted_list[3][0]

    first_percentage = int((sorted_list[1][1]/total_movie_number) * 100)
    second_percentage = int((sorted_list[2][1]/total_movie_number) * 100)
    third_percentage = int((sorted_list[3][1]/total_movie_number) * 100)


    # print the result inot a txt file
    # TIPs: Because the open way is 'a+', each time restarting the program,
    # the result will be written in the same file, if you want the different output file,
    # you need to save and delete the old one.
    with open("output.txt", "a+") as f:
        print("{}类高分电影数量排名前三的地区有：{}, {}, {}。所占此类别高分电影总数百分比分别为{}%, {}%, {}%。\n".format(category, first_location, second_location, third_location, first_percentage, second_percentage, third_percentage), file = f)

final_movie_list = []

# Main part of the program
for category in category_list:

    movie_numbers_dict = {'total' : 0}

    for location in location_list:
        new_movie_list = getMovies(category, location)
        final_movie_list += new_movie_list
        movie_numbers_dict[location] = len(new_movie_list)
        movie_numbers_dict['total'] += len(new_movie_list)
    # For test
    # print(movie_numbers_dict)
    dataStatistics(category, movie_numbers_dict)

# print the final movie list we have crawled into a csv file
# TIPs : while opening the csv file with excel, you need to choose UTF-8 encoding
with open("movies.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(final_movie_list)




