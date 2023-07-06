# 2D-to-isometric-converter
small python script for converting 2d tile to isometric tile
## you need pygame
```pip install pygame```
## How
- move the 2d tile images to the textures folder.
- If you need a specific resolution of the output image, change it in the line
  ```iso_texture = pygame.transform.scale(iso_texture, (595, 297))```
- the output images will appear in the textures/export folder
