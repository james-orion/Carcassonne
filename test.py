import tile

def tile_test_setters():
    """A function to test the setter methods of the tile class"""
    tile1 = tile.tiles[0]
    tile1.set_top(tile.Side['ROAD'])
    if tile1.top != tile.Side['ROAD']:
        print('Tiles Test 1 FAILED: Error with set_top method')
    tile1.set_left(tile.Side['CITY'])
    if tile1.left != tile.Side['CITY']:
        print('Tiles Test 1 FAILED: Error with set_left method')
    tile1.set_right(tile.Side['CITY'])
    if tile1.right != tile.Side['CITY']:
        print('Tiles Test 1 FAILED: Error with set_right method')
    tile1.set_bottom(tile.Side['ROAD'])
    if tile1.bottom != tile.Side['ROAD']:
        print('Tiles Test 1 FAILED: Error with set_bottom method')
    tile1.set_building(tile.Building['VILLAGE'])
    if tile1.building != tile.Building['VILLAGE']:
        print('Tiles Test 1 FAILED: Error with set_building method')
    tile1.add_shield()
    if not tile1.shield:
        print('Tiles Test 1 FAILED: Error with add_shield method')
    tile1.not_connected()
    if tile1.is_connected:
        print('Tiles Test 1 FAILED: Error with not_connected method')
    tile1.set_image("images/img.png")
    if tile1.image != 'images/img.png':
        print('Tiles Test 1 FAILED: Error with set_image method')

    print('Tiles Test 1 PASSED -- Setters work as expected (if this is the only statement about Test 1 printed)')

def tile_test_getters():
    """A function to test the getter methods of the tile class"""
    tile2 = tile.tiles[len(tile.tiles)-7]
    if tile2.get_top() != tile.Side['FIELD']:
        print('Tiles Test 2 FAILED: Error with get_top method')
    if tile2.get_left() != tile.Side['ROAD']:
        print('Tiles Test 2 FAILED: Error with get_left method')
    if tile2.get_right() != tile.Side['FIELD']:
        print('Tiles Test 2 FAILED: Error with get_right method')
    if tile2.get_bottom() != tile.Side['ROAD']:
        print('Tiles Test 2 FAILED: Error with get_bottom method')
    if tile2.get_building() != tile.Building['NONE']:
        print('Tiles Test 2 FAILED: Error with get_building method')
    if tile2.has_shield():
        print('Tiles Test 2 FAILED: Error with has_shield method')
    if not tile2.check_is_connected():
        print('Tiles Test 2 FAILED: Error with is_connected method')
    if tile2.get_image() != 'images/img23.png':
        print('Tiles Test 2 FAILED: Error with get_image method')
    print('Tiles Test 2 PASSED: Getters work as expected (if this is the only statement about Test 2 printed)')

def tile_test_rotation():
    """A function to test the rotation method of the tile class"""
    tile3 = tile.top_bottom_road
    tile3.rotate_tile()
    test_tile = tile.Tile(top=tile.Side['FIELD'], left=tile.Side['ROAD'], right=tile.Side['ROAD'], bottom=tile.Side['FIELD'],
              image="img22.png")
    if tile3.get_top() != test_tile.get_top():
        print('Tiles Test 3 FAILED: Error with rotation method top')
    if tile3.get_left() != test_tile.get_left():
        print('Tiles Test 3 FAILED: Error with rotation method left')
    if tile3.get_right() != test_tile.get_right():
        print('Tiles Test 3 FAILED: Error with rotation method right')
    if tile3.get_bottom() != test_tile.get_bottom():
        print('Tiles Test 3 FAILED: Error with rotation method bottom')
    print('Tiles Test 3 PASSED: Rotation works as expected (if this is the only statement about Test 3 printed)')


tile_test_setters()
tile_test_getters()
tile_test_rotation()