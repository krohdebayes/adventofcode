from typing import List, Tuple

raw_input = """
##........#.#.#.##.#.##...###.#.##.##.#.###..#...####..#.#.###.##....#....###..###.##..##.#.#..#....#.####..#####....##..#...##.##.....#.######.##.......##...#.#..##.#.#.#.######..##.###.#..#..###.##...#####.#....#.######.#.#..##..#.###...##.#...#.####..#.#.##..##..###..##...#.....####....###.##.#.##.#...##...#############...##.#.###.##.##.#.#####.......###.##..##..##.##.##.#..#.#..####..#####...#...#.###.##........#.##......##..###.##..#####.##........##..#.#..#.##....##.#.#..###.####.#..##...###..###.#...

......#.####.#...#..#..#.##.#...####.##..#..#..##.##........#..#####.##......#..#..##.##..#######.##
.###.##..#.########..###...#.##.#.#.#.##.#....##........#..#.#...#..#.##.##.######.##..#.#.###.###.#
.####.....##.##..#..#.#...#.###.#.###.#..##....####.#####.#..#.#.##.##.#..#..##..#.####.####....####
#.####.....#.###..#.##...##..#......#.#....#.####....#..##.........##.##########.##...##....#######.
.#####..##...#.####..####...#.#...###....#..##.##..#####.#..#......#..###.####.###.##......#....##.#
####...#.##...##..#..####.###.###.....#.##.##....#...#.###........#.#.#....#..#.###...##...#..#.##.#
###..##..###.#..#..#..#.###.##.#..###.#.#.....###.##......#..##.#...#.##..#.#########.......##....#.
#...#.#..##.#.###.#######.#...####.##.#.##.###.#.###..##.#.####..####...##.##.........#...#..#.#.#..
..#...##.#..#.##..#...#..#####.###..#.#..#..#..##.#.##.##.#####...######.#..#.###....##..####..##...
.###.####.#.#.....#.#...##.#....##.....###.###.########..##..###....######.##..##.###..#.......##...
....##.#.###..#.##.#.#.##...##.###..##.#..#...###.#...#...#..##.#....####...##.#.#..#..##.....#....#
#.##..##..##..#.##.....##.###......##..####..#..#..#..#.###.##..##.#..#.#...#.#.###.##.....#.#.#...#
...#.####.#.#.##...####.#.##..#.#.####..#.#...##..##..##....#.#.###...##...#.#.....##....##.#.#.###.
#.###...#.....##.#..##...#....##...###.##.#.##..#...#..####...####.##.#.######....#.###..#.##.##...#
..#..#..#..##.######.#..##.#####....##..##..##..##.#..####.##.##.#.###...#.###.####.#.....#.#....##.
...##.#.###....##..#######...#.......##..#.###.#...##.######...##.##...####..#.#.###.#...##.#.#.....
...##.#.....##.###....#..######..##.#...##.#....#####.........###..#.###.#.###.#......####........#.
#######...#####..#.#.###....###.#..#.#..##.#.#.##..#.#.##.#.#####.#.#.#########.##.##.#...#.##.###..
#.###.#.#.....#..###..#.#....###..#...#..####.#.....#..###..######.#.##.##.#.....#.#.#..###.###.....
#..##.#..#......#.#.#...#####.#...##..#.###.####..#...##.##..##...###..###....#.##......#....##..#..
#....##..#.##......###..##.#..#.#..##...#.##.##.#####.###.####.##.##.###...#..##.##.....#..#####....
##...#.#..###.#.##...##.#..#.#.......########.###.#.#....##.#..####..#.##.#.##.#.#..##.##..##...#...
#.###.##.##.#.#.##.###...##.##...##...####...###...#...##.###.###.##...#...##...#.#.####.#..##.##.##
##.#.##.#....#.#...###...###.##....#..##.######.###.....#..##..#..#.#.##.....###...##...#.####.#.#..
##..#...#..####.#.#..##..#...###...##.###.#..####...###..#..##....#####..##..#.##..####....##.####..
####..####..#..#.#.#..##.########......#..#.##.###.###.######........##.###.##.####...###.#####..###
##.#..#.##.#.....#........#.#.#..#.####.###..#.#..#.##...#.##.#.##.......##..####.#...........##...#
#.###.....##..#.#..####.####.#....#..#####..#..#...#..#..#.....####.#.#####.#.###...####.#...####...
#...##..#.##...#.#####.#.###.#######..#####..#..####..##.##.....###.#.####....#.#....#####...###.###
.##...#..###..#..###.#.######....#..#..#.##.###........#..##...#..#...#.#.#...###....#####...#.#####
#.#...####...###..#.#.##...##.###..####..##.###.#.#.#####...#...##.###..#.##..###....#.##....####.##
####.####..#..#..##.#.#..##..#..##....#.#.##.##..#.#.##.....#.#.#...###..####..##...###.#####..#..##
.##.##..#..#.##...####..##.....#....##.######.#..#..#..###.###..#...#.#....##....######....#..###.##
#.##..#.#.....###..##.###.###.####.#.#.##.#....##...#..#.###....##.......#..###...#.###.#..#..##...#
#..#.#####.####.##.#.#...#..##.##....#...#....##.#.##..#...##.##....##.#.##..#...###...##.#.##..###.
.#..####..###.#.##.##.##......#.##..##..###.#####.####.#.#..#######.##..###...###....#..#..#........
###..#.##..###..#.####.####.##.#..#####.##.#...##.#....#..#####...##.....#..#.#########..##..#.#..#.
##.#.#.##.......##.#####....##...#....####.....###.##.......##...#.#..#.#.##.###..###...#.##..##.###
#..#.##.#.##..#.###.....#....#.##..#....##.##..#.####.#####......#.#.#..#.....##..#..#.##.##.#...#.#
#...#.#.##....#.#.#.###.#.#....#..#.###.##...#...#..##.#..#...##...#.#.#####..##..#####.###...##..##
.#.#####..#..##.##...##.#..#.###.#.###.##.#...##..#..##.###.##....#####.#.##.....###.#.##...##..##.#
..#..####..#..#...#....#.##..##.#..#..#.#..#.#..#....####.#.....##.#.#####..#..#..######....#..#.#..
.#.###.#.#.##.#..#.###.#....##.....##..####...###.#.####...#.#.#..#.#.#..#.####.##..##.#..#.#..##..#
.###.###..##.##.##.##..#.######.####.####.....#..###......#.#........#.##.####.#..##....#.#..#..####
.##########..##..##.##.####.##.....#.#.#....##.###.#...#####..#.#..#.###.#.#...#.#....#######.....#.
#####..#.#...##...#....###...##..#..#..#.#.##.#.#.##...#.....##.#..#..####.#####....#......#.......#
#.##...#.##..#######..#.#####.#.##.##..#######.###.#..#.#..#.#.#.#...##.##.##..#....###...####.#...#
...##.#.###...##.##..###..##.####.#...#.....#..##.##.....#....#####.#..##.####.#######....###.##.#..
..##.#.....###..###.#.######.####.#####.##.#.####..###..#....#..##....#..#.#.#.....#...#..##.#..###.
#.#...###.#.#...##..##.#..##...#####.##...#####..####.#..#..#...###..#...#....#####.###.###.#...#.#.
..##...#..#.####..#...#..#.#..#.##...#...####....##.##.##.#.#..##.##....#.#..####..#..#.##..##..##.#
.##.....##.#.#...#....##..##....##...##........#..###.#...##..##..######...##...##.#####....####..##
.####...#..##.....####..#.#..#..####.##....#.#.#####..##...#....#..##.......#..#.....##.##.##..#.##.
##.#.##.#.#...#.#.##.#.####..#..#####.#.#..#.#.##...###..#...#.#.#.#..##.#..##.....##..#.###.#...#.#
#.#.#.#..#....##...#...##.#.###.#####.#..###.##.####.#.#.###...##.##.#..#.....#.#...####.##.#..##...
#.......##.#####..#.#####.######.#....##..###.#.#.#.##..####..#.#..#....#.##......#......#.#....###.
.##.#.#.....#....##.#.#.#.###.....#....##.#..#.##.#....#.###...##...##...##..##...##.#.#.#.#..#.##..
###.#...#.#.##.......#..###.#.##..#..#.##..#...##..#......#....#.#.##....#....##...###.#.###..###..#
.#..#..##...###.###.##...###.#.....#.##....##..#.###..#####.....#..####.###.##.#.#.########..##.#...
.#....#..####..##.#.##.....#.#.#.##.####.###.##.##..###..#....###.###.#.....#....#..#.#..#####.#..##
..#..#..####..##.###..#.##.....#..#..#.#..###..###...#..##...#.....#.###...#..#.##..#.#.#...##..###.
..#.#.......#..##......#...##..##.##..#.#..#.##...#.#..#.##.#..#.#...###.#......#..#....#.##.##.##..
##.##.#.#.##..#...#######.#..###...#.#.#.#.###.#....#..#.....#...#.#.###..#..###.##..#.##.##..#..#..
###.#....#..##....#...#...###...##.##.#.#.#.##..###......#....##..#.....########...#.#.#.####.#....#
####.##.####..##...#....#.#.#####.#####.#.##..###...#.##.#.###.#.##...#..##.###....#.######..##.##.#
.#......#..##....##...###...##.##.......#.#.......##....#.....#.......#...#.##..##....##...####..##.
.#.###.#.###.##..##..#.#######.##.#....##.#..###...####.##.#.....#..###...#....####.#####.##..##.###
#....#######.####.###...#####.###..#.#.....#.#.#......###.....#...#.#..###.#.##...#..#.##..#.#..#.##
.#..##.#..#.##..#..###..###.##...###.###..####...#####.###..#..####.#.#.####...###.####.#.####.##..#
#..###..##.#####.....#..####.##.#.##....##....###..#####.#.###....###..#.#..##.#....##.###.####..##.
.###.##.#.##.#.#..#.####.#...###...##..#.#.#.#..#..#.#.#..####.....##...#.#.#....#.##.###......#.##.
#...#...##...##.##..###..########.#.####.##..#..##.#.##...###..##.#.##.#.#...#####.#####...###.##...
.....#..#..##....####....#....#..###.##..#.#..####.###.....##..######.###..########.##.#.##..#.....#
..###.##.##.####........#....###.#.###.#.###..###.#####..###.#...#..#.####.#####.########...##.##.#.
.#.#.#.####.#.###..#..#####.##.#.#.####.#.##.#..###.##.#.#....#..##..##.#####.###...#..#.###....#.#.
###.#.#.#.#..#####.#.###...#..##.......#.##.#...#####.######......###..###.#....##..#...##.#.#...#..
..##.#.##.##.....###.....#.#.#.##...##..###.#.#.....###..##.#####.#.#..#.##..#..####.###...#.##.#...
#.###..#.....###.##......####.#......#.#..#.##.##.#..###.#.####.....#.#...#...#..#.##.#.....##.#....
.##.#.##....#..##.#.#...#.####.##.##.#.##.#..#.###.###.#.#...####.#.###....#.#.#..##..#.#..##....##.
..##..#.#..#.##.#..###...#.#.#..#.....##...##.#####.######..####.#...##.##..#.##.#..#.##...###.##.#.
..##.#..#.#......##..#.####..#...##.#.#..#.#.#.##.#.#......#####.##.##.####.##...#...#.#.##.#..##.##
#..#.#.#.####.#.#.#.##.....#.#..#.#..####.#..#.####..##..#.##...#.#####..###....#...#...#....##.##..
..#.......#.##.....##..########.##.#..#.....##...#..#..#...##..#....#...#..#......#..#####..#.##..#.
..#.##..#...#..#..#.##..#...##.##...#..#..###.#.#.#.##.##.#.#.##.#..#.##..#.#..###.###.#..##....#.##
#..#.#..#.##...#..##...##..##..#######.#...####..##..#.####.###.##.##.#....####.#..##.##..#.#...##..
.##...#.##...####..#.####.#..###..##..####..##..#.##.#####.#####.#.....#..#...#..##.##.##..####.....
##...#.######.#...##..###.#.#.#...##.#.#.#.#.#....##.##.###.#.#.#####.....#.#.##.........##..#######
.#.###.##.#.#..##..#..#.#..###.#.#.#.##.##.##..##.###..#..#..#...#####.###...#..#..#.#....#....#..#.
.##.#...#.###...#.####..##.##.#####.#.####..##....#..###...#..#..#.#.##.....#.##.#.##..........#.#..
####.#.#.#.#.####..#.....#..##.#...##.###.##.#..##..#..###..#...##..#.##..#.####.#..####.....#.#.###
.#.###...#.###..#.#.....#..#......#.#.#.##..#..#####....##..#.#..##########.##.#####...##.###...#...
.#.#.....##.####.#..#####...##.##.....#...#.##.#.####.#.##..#....#....#.#.#.#.##...#....##..##.##..#
.#....#.#.##..#.##.###...###....##........#.#....#.#.###.##.####.#..#.####.####......#...#.####...#.
#######..##....###.##..###..#..#...#.....#.....#...#..#.#######.#.#...#..#.###..###.#.#...###.....##
##..##..#..##...#.#.#.##.#....#.#.#.#.#..###.##..###.##.#..###..###.#.#.#....#.####..##...#...#####.
.#..#.#..#.#......#..####.###.#.#.##.#.#.####.###...#.##.#.##..##...#.#..#..##.###...#.#.########..#
#.#.########.#..#.#.##.###..##.#.###.#..#....####....##..###..###..#.#.#####..######.####.##..##.#..
###...##.#...#.#.#.#..##.###..###..##..##.#...####..#.#...#..###..#........##.#.##.###..#..###...###
###.#.#########.####.##...###.#...#.#..#.##.#..##..#.##.####...#.###..#...##..##...##.#.####..##..#.
.#...####..#...###....#.....#####.#.######....#.#####.#.##..##.##..#.##.......###.#............#.#.#
"""


def to_bool(char: str) -> bool:
    return {"#": True, ".": False}[char]


def from_enhancement_line(line: str) -> List[bool]:
    return [to_bool(val) for val in line]


def from_pixel_lines(lines: List[str]) -> List[List[bool]]:
    return [[to_bool(val) for val in line] for line in lines]


def get_input() -> Tuple[List[bool], List[List[bool]]]:
    lines = raw_input.split("\n")

    return from_enhancement_line(lines[1]), from_pixel_lines(lines[3:-1])
