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
player_rot_spd = 0.3

enemy_size = 10.0
enemy_spd = 2.0
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
sheep_fren_update_chance = 0.3 # Higher = update frens more but lag game more.
sheep_bucket_size = int( sheep_fps / frame_rate * sheep_count )
sheep_turn_spd = 0.3

# Add the following controls to adjust various elements in your game to help you debug
# (and to allow the grader to quickly and easily see that your components work):
sheep_vel_line        = True # Toggle Sheep Velocity line.
dog_force_line        = True # Toggle Dog Force line.
bound_force_line      = True # Toggle Boundary Force lines.
show_frens            = True # Toggle Neighbor lines.
show_walls            = True
bound_box             = True # Toggle Bounding Boxes.
enable_dog_force      = True # Toggle Dog Forces.
enable_align_force    = True # Toggle Alignment Forces.
enable_sep_force      = True # Toggle Separation Forces
enable_fren_force     = True # Toggle Cohesion Forces.
enable_bound_force    = True # Toggle Boundary Forces.
enable_obstacle_force = True

wolf_spr = "dog.png"
sheep_spr = "sheep.png"