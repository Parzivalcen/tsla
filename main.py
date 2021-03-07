import pygame
import sys
pygame.init()
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('track6.png')
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car, (30, 60))
car_x = 155
car_y = 300
focal_dis = 25
cam_x_offset = 0
cam_y_offset = 0
direction = 'up'
clock = pygame.time.Clock()
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    clock.tick(60)
    cam_x = car_x + cam_x_offset + 15
    cam_y = car_y + cam_y_offset + 15
    # get a px color in a particular position
    up_px = window.get_at((cam_x, cam_y - focal_dis))[0]
    down_px = window.get_at((cam_x, cam_y + focal_dis))[0]
    right_px = window.get_at((cam_x + focal_dis, cam_y))[0]
    
    print(up_px, right_px, down_px)
    # change direction
    if direction == 'up' and up_px != 255 and right_px == 255:
        direction = 'right'
        cam_x_offset = 30
        car = pygame.transform.rotate(car, -90)
# looks down
    elif direction == 'right' and right_px != 255 and down_px == 255:
        direction = 'down'
        car_x += 30
        cam_x_offset = 0
        cam_y_offset = 30
        car = pygame.transform.rotate(car, -90)
# left turn
    elif direction == 'down' and down_px != 255 and right_px == 255:
        direction = 'right'
        car = pygame.transform.rotate(car, 90)
        car_y += 30
        cam_y_offset = 0
        cam_x_offset = 30 
# up turn
    elif direction == 'right' and right_px != 255 and up_px ==255:
        direction = 'up'
        car = pygame.transform.rotate(car, 90)
        car_x += 30
        cam_x_offset = 0
    # checks if road px is white if not stops==drive
    if direction == 'up' and up_px == 255:
        car_y = car_y-2

    elif direction == 'right' and right_px == 255:
        car_x = car_x +2

    elif  direction == 'down' and down_px == 255:
        car_y = car_y+2
    


    window.blit(track, (0,0))
    window.blit(car,(car_x,car_y))
    pygame.draw.circle(window, (0,255,0), (cam_x,cam_y),5,5)
    pygame.display.update()