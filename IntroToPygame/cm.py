from vec2 import vec2
import pygame

# CM = Constants Manager
frame_rate = 60.0
screen_width = 800
screen_height = 600
screen_size = vec2( screen_width,screen_height )
bg_color = ( 100,149,237 )

player_size = 10.0
player_spd = 5.5
player_col = ( 255,255,0 )

enemy_size = 10.0
enemy_spd = 5.0
enemy_col = ( 0,255,0 )
enemy_attack_range = 200.0

enemy_hunter_col = ( 255,0,255 )

align_force = 1.0
cohesion_force = 1.0
separation_force = 1.2
bounds_force = 1.7
dog_force = 1.0
sheep_neighborhood_dist = 200.0
sheep_bound_dist = 50.0

wolf_spr = "images/collie.png"
sheep_spr = "images/sheep.png"