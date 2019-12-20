from w2e import scrapper
import matplotlib.pyplot as plt
import urllib

def display_suggestion(recipe_suggestion):
    f = urllib.request.urlopen(recipe_suggestion['img_link'])
    img = plt.imread(f, 0)
    plt.title(f'{recipe_suggestion["title"]}\n{recipe_suggestion["link"]}')
    plt.imshow(img)
    plt.axis('off')
    plt.show()