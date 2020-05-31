import pandas as pd
import matplotlib.pyplot as plt
import os.path
import pygame
import time

def isDirEmpty():
    path1 = 'plots'
    isdir1 = os.path.isdir(path1)
    if (isdir1):
        return False
    else:
        return True
if isDirEmpty():
    df1 = pd.read_csv("city_populations.csv")

    #selecting particular columns
    df = df1[['name','group','year','value']]
    year = df1['year']
    df = df.sort_values(by=['value'],ascending=False)

    #selceting rows with year curr_year
    count = 0
    for i in range(1575,2020):
        curr_year = i
        #create a variable with true if year == curr_year
        curr_population = df['year'] == curr_year
        curr_population = df[curr_population]
        print(curr_population)

        # drawing the graph
        fig, ax = plt.subplots(figsize=(10, 8))
        values = curr_population[::-1]['group']
        clrs = []
        for x in values:
            if x == "India":
                clrs.append("#adb0ff")
            elif x == "Europe":
                clrs.append("#ffb3ff")
            elif x == "Asia":
                clrs.append('#90d595')
            elif x == "Latin America":
                clrs.append("#e48381")
            elif x == "Middle East":
                clrs.append("#aafbff")
            elif x == "North America":
                clrs.append("#f7bb5f")
            else:
                clrs.append("#eafb50")
        # to flip barh
        ax.barh(curr_population[::-1]['name'], curr_population[::-1]['value'],color = clrs)
        ax.text(0.95, 0.15, curr_year, transform=ax.transAxes, size=46, ha='right')
        plt.savefig('plots/{}.png'.format(count))
        count+=1
        plt.close()
        print("*************")
pygame.init()
width = 1000
height = 1300
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Racing bar graph")
clock = pygame.time.Clock()

def graph(count):
    img = pygame.image.load("plots/{}.png".format(count))
    window.blit(img,(10,10))

running = True
count = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            window.fill((0,0,0))
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_s:
            for i in range(445):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                graph(count)
                pygame.display.update()
                time.sleep(0.2)
                count+=1
                clock.tick(70)
            time.sleep(2)
            running = False
pygame.quit()


