from vec2 import vec2
import pygame

# CM = Constants Manager
frame_rate = 60.0
screen_width = 1024
screen_height = 768
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

align_force = 0.5
cohesion_force = 0.6
separation_force = 0.6
bounds_force = 0.8
dog_force = 0.6
sheep_neighborhood_dist = 70.0
sheep_bound_dist = 60.0
sheep_count = 100
sheep_fps = 12 # Higher = more sheep responsiveness, less game fps.
sheep_fren_update_chance = 0.9 # Higher = update frens more but lag game more.
sheep_bucket_size = int( sheep_fps / frame_rate * sheep_count )

# Add the following controls to adjust various elements in your game to help you debug
# (and to allow the grader to quickly and easily see that your components work):
# 
# Toggle Sheep Velocity line
# Toggle Dog Force line
# Toggle Boundary Force lines
# Toggle Neighbor lines
# Toggle Bounding Boxes
# Toggle Dog Forces
# Toggle Alignment Forces
# Toggle Separation Forces
# Toggle Cohesion Forces
# Toggle Boundary Forces

wolf_spr = "images/collie.png"
sheep_spr = "images/sheep.png"