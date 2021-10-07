# random article generator


import wikipedia

print("Wikipedia Articles")

random_articles = []
class random_aricle_generator:
    # get the 10 random articles from wikipedia
    def generate_random_articles(self):
        global random_articles
        random_articles = wikipedia.random(pages=10)
        print(random_articles)

    def show_article(self):
        # ask the user if he wants to read any of the articles from the fool. list or not
        print("Do you want to read any of the article from the above list? Y/N")
        response = input('Y') or input('y')
        # if 'Yes' show the article otherwise again show the random articles
        if response == 'Y' or response == 'y':
            print("please enter the which article number do you want to read.")
            article_number = int(input())
            print(wikipedia.page(random_articles[article_number]).content)
        else:
            rag.generate_random_articles()
            rag.show_article()


rag = random_aricle_generator()
rag.generate_random_articles()
rag.show_article()


