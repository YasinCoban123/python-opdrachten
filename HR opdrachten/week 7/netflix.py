import os
import sys
import csv


def get_headers(file_content):
    return file_content[0]


def search_by_type(file_content, show_type):
    type_index = 1
    return list(filter(lambda show: show[type_index].strip().lower() == show_type.lower(), file_content[1:]))


def search_by_director(file_content, director):
    director_index = 3
    return list(filter(lambda show: show[director_index].strip().lower() == director.lower(), file_content[1:]))


def get_directors(file_content):
    director_index = 3
    return set(show[director_index].strip() for show in file_content[1:] if show[director_index].strip())


def load_csv_file(file_name):
    file_content = []
    with open(os.path.join(sys.path[0], file_name), newline='', encoding="utf8") as csv_file:
        file_content = list(csv.reader(csv_file, delimiter=","))
    return file_content


if __name__ == "__main__":
    csv_content = load_csv_file("netflix_titles.csv")
    header = get_headers(csv_content)

    menu_item = input("Enter a menu item (1: Count TV Shows, 2: Count Movies, 3: Directors with both types, 4: List each director with movies and tv shows): ")

    if menu_item == "1":
        tv_shows = search_by_type(csv_content, "TV Show")
        print("Total TV Shows:", len(tv_shows))

    elif menu_item == "2":
        movies = search_by_type(csv_content, "Movie")
        print("Total Movies:", len(movies))

    elif menu_item == "3":
        # Find directors with both TV Shows and Movies
        directors_with_both = []
        directors = get_directors(csv_content)

        for director in directors:
            director_shows = search_by_director(csv_content, director)
            movie_count = len(search_by_type(director_shows, 'Movie'))
            tv_show_count = len(search_by_type(director_shows, 'TV Show'))

            if movie_count > 0 and tv_show_count > 0:
                directors_with_both.append(director)

        print("Directors with both TV Shows and Movies:", sorted(directors_with_both))

    elif menu_item == "4":
        # List each director with the count of movies and TV shows
        director_counts = []
        directors = get_directors(csv_content)

        for director in sorted(directors):
            director_shows = search_by_director(csv_content, director)
            movie_count = len(search_by_type(director_shows, 'Movie'))
            tv_show_count = len(search_by_type(director_shows, 'TV Show'))
            director_counts.append((director, movie_count, tv_show_count))

        # Print each director's record as a tuple
        for entry in director_counts:
            print(entry)
