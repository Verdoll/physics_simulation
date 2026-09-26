def object_surface_y(object, surface):
    if set(object.get_pixels()) & set(surface.get_pixels()):
       object.crash_with_floor()
    else:
        pass