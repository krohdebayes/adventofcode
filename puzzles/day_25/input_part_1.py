from typing import List

raw_input = """
>.>.>.>>>vvvv>>v...v>>.vv.v>>>>>>.v>....>>.v.v.>>....>.v>v>..vvv.v..vv..v>..v.>.v>v...>..v>>v.v......>vv...>>..v>.v>.....v.>.v.......>.>>.v
.>>....>>.v.>.vv..vv.v>..>...v..>...v.v...>v.>>.vv..>...>>..>...v>....>...>>.>..>...>.v.>..>v>.>>v>...>.>..>.v.>..v>>vv>v.v>>vv.v..>>v>.vv.
vv>.vv>>vv......v.....v..vv.v>....v>.>v>.>.vv>..>..vvvv>.v...>>v..vvvvv>>.v....v.>..v>>>....v...>.vv>...>v>.v.vvvv.>>..>>..>.>>.>v.v.>v>>>.
v>.v.>>>>.v...v.vv>.>v>.v>v.>>v.v>>...v.v.v...vv.>vv>v>>.vv.v..v>>.v>.>..>.v.v..>v.v>...v..vv>.>vv...>.v>..>.>>..v..v..v>..v.v...v>.>vv.v..
.>>>...v...v.vv>.....v.>vv>>.>>..>..v....vvvvv...v>.v.v.vv.vv...>...vv.v.>v..v>.>.v..v.v>v>...v...>.>.>>>..vv...>v>>.>>v.>..>.>v.v.v.vv.v.v
>.>.>..v.v.>>..>..>..>v..>.>.v.>.v>>>v.v>v...>>vv.>>>>.vv...v>......v>v....vv..v>..>.v>..>.v>.>>..>.>v>v>v.v.>..>..>..v..>>...>.v>...v.v.vv
>.>..>>.v..>>.v>v.v...>>v>v.>...>.v.>v........v..>>...>..>v.>v..v.vv..>v.>>vvv.>>>>>v>v.vv.>..>v>>>.vv.v>vv.v>...>>>...>..>..>.>v..v..vv>..
>>.>>v>.v.......v.vv..v.v......v.v...>..>..>>>..v>...>.....vv..>>.>.vvvv>....>vv..>.>>v.........v.>>>>....>.>.>..v>...v.>...>.>>>..v.v>>.v>
>v.vvvv.....>v.>.>>vv.v.v...>>.>.>v.v..>v..>v>>.>..>.>v.v..v>>.v>..>...v.v>vv>.vv>v.>v.v..>>.vvv>..>..>>v..v..>>.vv>..v.>.v.......>..vv..vv
.>.>vv..>.>.>vvv.....vv>>....>.>>....v>vvv..>>v.vv>.>.>.v.vv.>....v>..>........v>v>.v....>v>>...vv.>..vv.>>.v..>.v>>.>>.v>.>.>vvv.vv..>..>.
>>v..vv......>>v...vv.v.v.>>v......>>v.>..>.>vv>..>.v>>...v.>......v...>..>.>vvv..>v.....>v.>v..v......v..>...>>v>.v...>v>v.>>..>v.>.v.vv>.
.vv>.>.>.v>..>>....>v>.>.>>>>.......v>v.v>....>>.v..v........>>.>>vvv>..v.vv..>.>....>>vv>v..v>>..>..v>.>>.>.>v.>.vv.>...>.vvv>>......>.>>>
v.v...v.v...v>v.>>.v.>.>vv.v.....v.>>>>...>.>..v..v>....>.v>.vv>....vv.>>..v>vv>..>.v>.>v.....v.v>.>.......v..>vv....>.vvv.v..>>v>...v.v..v
.>v>v.vvvv>.>vv.vv.vv.>v....>v>..>.v.>>..>>.>>>>.......>>>..v..>>...>>>.>vv>v..>...v..v..vv.vv...v....>...v>..>.>.>.>vv..>.>.>..>..v.v.....
>.>...>>vvv.v..>...>....v...v...v..>v.....v.>v.v..>.v>>..>.vv...>...v..v>v...v...>.v.v>vv..>...........v.>>.v>>.>vvv.v.>>>>..>v>v>>>.>>..>.
..v>v..>>..v.>...v.....>...>..>>>v..vv>...v.v.v.v>>>.v.vvvv.v..>>.v.>v>..vv...>>>.>...>>v>.....v>.v.......v>.>v...>.vvv>>..>v...>..v..v>>vv
.v.>v>vv...v...v...>.>...>.v.>>v>..>>.>>>v.>.v.>>.>..v.>vv>v..>vv>...>..>v....v.>>v....>.v.>>.v.vv>vv>.v.>>v.v>..>..vv.v>.v>v>v>..>.>...>>.
.v>>>.v..>.v.>>.v.>>vvvv.>>v..vv..>v.>.>...vv>.v.v>v>v..>.>>.vv>...v>.....>>vv.>v.>.>..v...v..v.v.>>v.>....v..v>vv>v..>vvvv...>.>.....v.v.v
>....vv.>.v.v>>>v....>..........v..>.v..v....v..>.v.>.vvv>vv>v.......>..>v......v>vv...>...>v>>>.>v.vv.v.v>>.v.v>.v.>.>.v.>v...v......vv...
.v.v.>vv.>.v>.v..v.v.v.>>......>.v.>>.>>.v...v.>>>v.....>>>..>.v..>>..>.v>>.>v>..>...>.v...>>..vv.>>>>>>>>....>>...v.vvv>>..>>.>..>>v.v.vvv
.v...>.>>..v>>>v.v.....>.v>.>>>>...>>..v.>.v.........>v>..v..v>v>...v>v>...v....>..v>.>...v>vv>>>...v..>.vv.>v...>.>..........vvv.>vv.>.>vv
>>>>vvv>>v.>.vv>v>v....v>.v>...v>>vv..>v...>>.v.>....>.v.v>.vv...vv....vv....>..v>.v..vvv...>>.vvv.>.vvv.>.>>..v..>>.v..>>.>v>v>>...>.v.vv.
>.v>.>v.v.>.v...>...>>.>...>v.v.vv..>.>v.>vv>.v>...v>.>...v.>>..>v>>>>.>>.>>v..>.vv..>.>..>v.>.v>>>....>.>..vv.v>vv>.>...>>.v..>>...vv.v..v
v.>v>..>v..>>..>.>>.v.vv.vv.>.>>v>.v>vv.>vv.>vv..>.v...>>.vv...v..v.>.v.>.....>v...>..>.....>.>>v.......v...v.v.>.>...v.>......>.>...>>.>.v
>vv>..v>v>v>.>>v>...vv...>>>vv.>.vvvv..>.v.>>v>vv.>..>>..>v.>..v.v..>v..>>v..>...>.>.>..v...vv.>v.vv....>>v.v>....>...>.v..>v.v.v...>>>>.>>
.vv.v...v>vvv.v>...>v....>..vvv.vvv.v.>>v...>>>.>..v....v>>>v....vv.v>.>..v..>.....>..>>..vvv>>vv...v..>.v>>...v>v.v.v.>v.v.v>>..vv..>.v..>
.>..v....v....v>>.>..v>.>>..v>>>.>v..vv.v>vv..v.v>.v.v...v>>...>>vv>>vvv.>.v.>v..vv>>...vv.......v..>vvvv>>.>...>.v>>vv..>...v....v.....>..
>>>v.>>>>>.v.vv>...>..>>>.>....>v>>....v..>..>v.>>.v>.vv....>...>.>..>..v...>>v...v....>v.....>>.>.>>>.>>.>..>>.>>>>>.>v.v>>vv>>.>>>.>vv...
v>...v.>v>v>>.vv.>v.>v....v>.>v..>...>>>v....>..>...>.vv>>.>...>vvv...vv.v.>v......>.v>vv.v.vvv>>..v>>.v>.v..vvv.v.v.>>.>>v.>.v.>.>>v..v.vv
>>.>..vv>>..v>vv>>>v..>..>...>..>v.>...>>>..v..v.>vv>.>.....v.v>.>>.v>v.>..>.v...v>..v>........>>.vv...>.v..>>v>v..v.>v>>>...>.>>..>.vv>v..
>v>v....v..>...>....>....>..>...>..v>v...v..v....>.....>.v..v....v.v..vv......vv.>vvv>..vv>v..v>v.v>v>.>....v...>>>>>..>..>.v..v..v...>vv.>
.v.>v..>..vv.v.>.v.>>>v.vvv....v>....v.v.v..v....v...v>v..v...>v.>v..>.v>..>>..>v>.vv.v..>.>>v>.>..>>>v.v...>.>....>..>..>v.......>v>v.>.>.
vv.>..>v>>.>.............>.>v>..vv>.vv>..>>.>..>....v>>v....vv>....v>.>.v.v.v>....v.>.vvvv>vv.v>.>v>vv>>..v..>>...v>..>>..>>..v.v..v...>vv>
>.>.>..>>...v.vv.....v..v..>...v.v..>>.....v>>...v>..vv..>>.v.>>>v.>...v.v.......vv.vv...>>...>>v>..>.>vvvv..>v....vv>.v>>v..vv.v>>vv.>v>.v
..vv..>..v..v.>.>.vvv..vv..>..v>v.v.>.vvv>vv.>.......>>>vv>>...>v.v.>>vvv..>..v.>v..>vv>v.vv........v>.>....v.>.....>.>>v.vvvv..v.>..>..v.v
...v.vv>>.v>..>.>>vv..>.v>>..>vvvv.v..>.v.>>....>.>..>>.v>...>vv...v.>>vv..v..>vv>.>.v>.vvv>>.>.v.v...>...>v.>.......v.>.v>.>.v.>.>.>.>.v>.
vvvv.>v>.>>..>...vv...v>.v>>.>.v>.>vv...v..>..v.v>>v>.vv.......>...>v>v.v.v>>...>.>v>.v...>.>.>>..>vvv>>...v.v..>v..v>..v.>v.v.>.v.v.>v.v.v
>.>...v..>..vv.vv.>.v>..v>v.v.v.v.>...v>v..>v.v>v>v>.>.....v.v.>..v..v.v.vv.>>>.vvvvvv.>......v>>>v.v>v....vvv>.>.>.>v..>..>v.>..v.....v>v.
v.v.v...>.>..>.v>..v.v.vv..>.>.>..>>....v>>..>.>v....vv..v...>>v.>....>..v>.v.v.>.>......>v>v.v..>.>>.>v>...>...>vv........>vvvv.>v>>...v..
.v....>vv.vv.>v.>.vv>..v.>...>v...>vv>..vvv>.v...v.>..>v>>v...vv.vv....>>.>..>v>..>>...vv..v>.>.v..vv.>.v..v..>.v.>>..>>v.v..vv.v.v.v.v.>v.
>>...>v......v..>.>.v.vv>>.>...>v.....>v.vv>.>.....>vv>.>...>vvv>..>>.>....>>.vv.v.>v>v.v....vv....>...>>...>...v>.>..v.>.vv.>vv>>vv.v.....
.>.>..v....>.>.>v.>v>..vv..vvv......>v..v..>>>.>v>>>...v.>.v>vvvv.v.>>...v.>v.v>..v.>vvv.v...v>...v.v>v.>.>.>v..>v.>.>vv.>vv>>>.>>>>v>v..v>
v..>..>.v>...v......vv>...>v..>.v>...v.v>...>.>>.v>...>...v..>>...>..>..>>..vv.v.>v.>>>..>>>>..>>.>..>.>>..v.v>.....v.v>v>>vv.vvvvvv....>v.
..v..v>v....>...vv>v....v>v...>>.v.vv.>>v.vv.>vvv.......>..v.v>>>..>..>>......>>......v......v..v....v...vv..>>.v.>......v.>>...v>..v>>v>vv
vv..v...>>.v>.>.v...vv>>..v...>.v...v..vv>>..>..v>.v>vvv>v.>.vv.v..>.v..>>........>.>.>.>vv...>..v..>v.v>.vvv....>....v>..>>v>>vv>.>..>v...
.>>>.>.>>.vv.v....vv.v.>>.....v.v>...v>>>.vvvv.vv.>.v>v.vv.vv>>.vv..v.>>.vv>>vv>.v..v.>v.>....vv>....>v.....v.>..>..>v.>.>..v>>.v>.>>vvvvv.
v>>..vv>.>.....>vv.v..vv.>>.>>...v..>....>.vv.>>...v.>v>....vv>>....v>...v.>..v>.....v..>.v.vvvv.v..v>>.v....>.v>.>>..vv.>v>..v>.......vvv.
.vvv>...>v>..>>...>.....>...v..v.>>>.v>.v..v>>>>..>..vvv>.v..>v...v>v.>.>.>.>.>.>>..v.>.v..vvv>v>.............v.>.v.v.v...v.v.>v...v.>.v>..
>..vv>...v.>>....v..v..vv..>>.....>v..>.....v>.v..v.>.v>.v>vv.v.v>.>.>.>>.vv>v>.v>.>......v>v..v>v.v.>>v>.>v.v>v.v>>>v>..vvv>>.v.v>>>v....>
.v.....>v>>....v..v>v...>v.....v.v.>..v>v>v>>>..>.>v...v..>v.v...vv..>....>v.>>>v..v.v>vvvvv>v>...v...>>..v.v.v>vvv>v.>v>.>v.v...>.....v..>
>.v.>.vv.>v.v>>>v...v>>>.>...>vv..>.v>.v.v...v.>....>.vv.v..>>.>....v...>....>.>>>v..vvvv.>vv.vv.>>>>..v>v>..>v>.v.>...>..>.>.vv.>>.vv>.vvv
.v.>v>v>....v.vv.>v.>...v>.>>.......>>.v.>v>.>vvvv>>vvv.v>>v.v.>.>.vvv>.>v....v...v.>v.vv...>>>vv..vv..vv...>..>>.v....vv>>>v..v.v......vv.
vv..>..v.>.v.>v..>..vv.>...v.>vvvv>v.>vvv.>.>..vv.>.>.>...v..>..>v..>...v>.>v>.v.v>>..>..vv>.v....vvv>.>.>>.>>..>v>>.v>.v.>>..>>v.>>.v...v.
v>>>v>..vv.>>..v>.....>vvv.>>..>.>>.>v.>vv.>.v.v...v....>>.>..v.>v..v>...>.v...v.>>.>v.v.v.>vv>...>............vv>>>v>v>...>v>>.vv.>v...>>.
v.v....v>vv..>..v...>....>>>..vv>...v..v>>v...v.>v..>..v..>.>....v.>vv>..v>.>.vvv>..v>>.v.v>.>..v.>v..>....>.>>v>vv.....>...v...v....>>.vv.
...>.>>>>v.v.v..>>....v>.v..v>v...>>vvv.v>v..v>vv...>.v>.v>.>.v>...v.>.vv>..>....>..>>vvv.v....v.v>>>v.>>>>.>v.v.>>.>>...v..v.>...v.v>.>>..
>....v..>....v.vv.>.v>v.>.vv..vv..>.v.>v>.>>>..>..v...>vv>vv>>v.>..v>>.vv.v.v..v>>.v.>.>...>.>..v.>.>......>.v.v>>.>.>>..v...v>.v.>>v..>>v.
vvv.>......v.>v....v>v...>.....v..vv..>>v>.v..v...v.>.>>..v.v..v>..>.>vv.v>>>vv>..v.vv......v.v.>v.v..v..>..vv.v.v>>>....>..v.>v>...>.>....
.v.>.v>>..>....vv>v>vvvv.v.>.>>...>.>.v.>v..>>v..v>.>..>.vv..vvv>v.>..>..v....>v..v.....v>>>..>.v..>vv...v.v....>vv>..v.>v>.>vv>v>v>>v>>>.v
>vv.>..v>>v>v.v>.v..v.v>v>.v>.>.....vv>>>>...v..>vv>.v>>v.>.>....>...>...v>>.v.v.>...v.v>v..v>>...v>>>...>...v.>v.>>..>v.v>..>>>vvv..v>.>..
v>>>>.>.v.>v.v....>....>...>.>.....>.v..v>.>v>.>>v.v>...v..>>>.vv...>..v..>>..v....>v....>v.>vv>v...v>.vv>.v>v>..v.v.vv..v...v..>>..>v>.vv.
v.vv.>.v.....v...v.v...vv.v...v>..v.>....>.v>.>>vvv>.>.v>...>.vv>v...vv.v..>vvv...v.>..v.>.>>>.vv>v.vv.vv>v>v>>vv>v.>>vv..>..vv...>v.v>>..v
...>>vv>>>>vv.>>v>v>.v>.v..v...>>..v>...v>>vv>.>.>.>>..>....>vv.v.vv.vv>.>v..v.>..v.>.vvv..>..v...v>>v>..v>>v...v..>>...>>vv>.v...v>.vvv...
...vv.>>.v...>>..>v>..v.v>..vvv>v.>>>v.v>.>...vv....>>>.v.>>>>v.v>vv>>....>>.>..v>vv>....v.>.>v...>.>v.>v>.v..>>..>v>v>..>..>v.>...>....vv>
...v>.v..>v.v......v>>>........v.v>v..vvvvv>..>.vvvvv>>>.vv.vv>v...vv..>v>v.>.v>.>....v.>..v>..v..>>vv>>......>............>>>vv....v>v.>.>
..>...>....vvv.v......v.>>>.....v.v.>...v.>v....v...v>..>>>..>..vv>>v.v>.>.vv.vv.>.v.>v>v>>.>>v..>......v..vvv.>>....v>v.>>vv>>..>..v>>>.>v
.v>.....>v...v.v>..v>..>....v...>..vvv>...vv.>v.>...v>.v.v>....v...>>.v>>v...>>.>.v.v.v>v.vv>v.v.v..>>.v.>>.....>>>...vv.v>....>.>.>v.>v>.>
>..>v.v.v>..>vvv....v....v>v.>...vv.>v>....vvv.....v>.vv..>..>>>v>v>v.>v.v>...v.>...vv.>....>>...>.v..vv>v>.vv.v....v>v>v>.>>.>>.>>vv...vv.
vv>........v>v>.v.v>....v.vv.vv......>.>>v..>>>.>.>v...vv.....>>>.>.v.v...>.v.v..>.>.v.v.....>.vvv>>.v.>>.........vv.v..v>v>v>.v>>..vv.v...
.>>.vv.v>>.>>.>>..vv...v.v>v.>.v>>.vv..v...>...v...vvv>>.v...v.v>>>v...v..v...>>..v.>>v.vvv>...v.........v.vv>..v.v..>..>.>v>.>.>>..>v..>..
.v.v..v.vv>v.v...v..v>v>.>v.v>v....>....>v.v.>>..>>v>>.v..v>v.>>.>v.>..v....v>..>..>.v>..>v..v.....>.vv..>.......v>....vv..>v..>>v..>v....v
v.vv.v.>v.>v.>...v.v...v..>..v..>>.vv.v.>.>...>>.>v>........>>v...>.>v...>..v.>>v.>...>..>..v>>vvv>.....>vv>....>......>>>vv>.>>..>>>..vv.v
>vvv>v>vvv..v..v..>>.v>vv>......>>v.v>.>.>vv.>.vv..v..>.v>.....>v.>....>>v.vv.>>.v...vvv....v>>>..>..>.v.vv.v>v.....vv>..>.>.>>..v..>.>..v>
.>....v>...>>>>........v..vv>v..v..v....v>>..v.vv...>.>.>..>.....>v>.v.v>v...>vv.>..vv..v>v>>v.>>.v..v>.vv>.v....v>v>..>...>..v..>..v..>>..
.>.>v>.>v>..>vvvv.v.v.>.v.v.>>...>vvv.vv..>>>.v>.>.v..>v..vvv>...>v>.>v.>>v>v>..>v........>v.vv.>>...v.v..vv.>...>..>..v..v...v.v.v.>.>vv..
............>v....v.vv>>v..>...>.>>>..v>.v.vv....>.>>>>v>...>v.v.>v.v.v>.>...>>.....v....>.>...v..v..>..>>.>..v>>v.v..>.>vv>v.>..vv.vv..>v>
.>..vvvv>vv.>.>>v.>.>>vv>vv>..>>v>.>...>>v>v..>>.>v..v.v>>.v>....>v>.v.>>>.v.v..>>.v>>.v...v.vv.v.>..v>..>...v..v..vv>.v....>.>>....v...v>>
v.v>vv>....v..v>>.>v.v.vv>>vv>>.>>..>>vv>..v..v>.>......v..v.....>v...vvv.v...>.vv>...>.v..vv...v>....v>v..v.v>.v...vv...>.v..vv.v>.>v>>.v.
>...v.>>v>..>.>..v.>vv.v...v>..>>...v>>vv..v.>.>v..>...v.....v>.>..v>>...v>>>.>..vvv.v>.>>.v>.v.v.>v>vv.vv>.v.v..........v>>..v...>..>>>>>.
v.>>.vv....>.....vv>.>.>>>.v.>.>>..vv..v.v.>...>.>>...vvvv..v.>....v.vvv.v.>v....v>..>>vv.v.>>..>>.v>.>v.v...v..>.>.vv>.....v.>.vvvv>>vv.>.
>.>v>..vv..>..>>v...v>...v.v..vv>.....>.>...>v.>..>...v>v....v.v..>>v...>...vvvv.>v..v>..vv.>...>>.v...>>..>..>v.>>>>>....>.v..vv>vv.v.>.>v
>...>v.>>>v>v>>v.v.>v..>.vvv.vv>>.vv>...>>.v...>.>>>...>....v.......>.>.vv>v.v.>>..v>..v>vv>...>.v>vv...vv.v>...>.>>v.v>v.v.>.>..vv....>...
vv.vv...>..>vvv...>v.vvv>.v.vvv...>.v>.v....>v>>>.v....vv....>..>vv>.>....>.>>vvv.>....>....>>...>v..>v>>v>>v.>v.>..>..v>>v....>......v.v>.
.>v..v..>.>..v..>.....v>...vv>.vvvv..>..>v..v>>.>..>.>.>..>>...v>>.v.v.>v.>...v..v.>v.vv.>vv.>..v.>v>.>.>.....v.....>.....>>>v.>.>>.v>.v>>.
vv.>....vv...>v.v>.v>>..v.....vv>..v>>.>..>.v...v..v.....v>>>.vv>>..>..vv.>>....v..>....vv>>>..>vvv..vvv>v>.>v..>>.v.v>.v....v.>>..>....>v>
.....>...>.>..vv>....v.v.>v..v.vv...>.vv.v>>>.>>..>v>...v..>.>v.>>.....vv.>v.>>.v>....v>>..........>.>v..v.>vvv.v.v>.v>.v>>.>.>>.vv.>>.v>v.
...v.v...v.v.v>v>.vv.>>.vvv>>.v>v.vv.>.>....v...v...>>>>>>>>v....vv>.>.>>>..vv.>....>>.....vv>......>.>>.......v.>>>>>.>>.>v.v......v..v>.v
...>vv>..v.>v>vv>.>vv>...>...vv>>.>.v>..v....>vv.>.v.>>v.>>.>...v.vv..v..>.vvv.v>v.>.>.v>.>v.v.vvvvv>>.>>..v>....>.v.v......v....vv..v.vv..
>vv>.v..vvv>>....>v>..v>...v.>.>vvv..v......>vv>..v.v.>>....>...v....>..vv.v.>>>v.v.>>..>.>vv>>..v>.vv..v>>v.vv>.v>.v.v.v>..>.>.vv.v>v>.>.>
>.vv...v..>..v.....>v>>.>.>v>...>>..v>....>>..v>....v.>.v...>>vvv>...>>..v..v>vv.v>v.>....vv>v.>..v.v>v...>>.v.vv..v...v.v.>.v>.>..>.>vvv..
>>v>v.>.>vv..v.>vv..v.....>v..>v...v.>v.>>.>>>.v.>vvvv..vvv..v>>.>...>>.>..>.>...>v...>...>v.vvv>......>v....>.>>.v.>.>>v....v.>.....vvv>v.
...>>v..v>v.>.>......v>.>>.>vvv..>>.vvv.>.v>..>v.v.>>.>.>..v.>..>v.>>.v.>>.>>>v.>..vv..v>v.......>v>..>..vv>v.>.>....>>....v...v...>vv..v.>
.v>.>>....>>>v>>>..>..v..>...v>v>..>.v.>....v..v.v..>vv>>.v.vv.vv.>>.vv.v.v.>>>>....>.>...>>...v>.v>.vv....v>>>.v>v.>.vvv>..v...vvv>>.vv.v.
v..v..>..v.>>....v.v>.>..v>..>>>>..v>..v.>.>>>v>vv>.v>.>>>..>>v>>.>.v..v....>..v>>v.....vvv.v>.vv..>...vv.>>.>.>.v..v>>v.v...>..>>...>v..v.
>>.>v>v..>>...v>.>vv.v>.>.>>.v...v.>>v>>>.v>....v..>..>..vvvv>...vv.>...vv...>.v.>v>>>>v>..>>...>>v..v>>>v..>..>vv>.v..v.v.>.>>v.vvvv..v.>>
.>v.vvv...vv.vv.>>.>....>..>vv>..>.v.....>.>v>>>..>>v..vv....>>.......>>>v.vvv>>.......>.>vvv>.v>>....vvv..>vvvv.>>v..>.....>..>.>.>.>v.>>.
>.v....v>.>.>..>.>.>..>v.>...>....>>>v.....>>..v>>>.v>>..>.>v...v.>...>.>v>..>.vv>.>v>>.>.>>...vv>.>>.vvvv.v..v.....>>>vv...>>.v>v..v>v....
.v.v.>..v.>..>.v.>v.v.v.>.vv>v..>>v>.vv>.vv......>v...v>..v>..>>.>v>.>.>v.>>.>v.v...>>.v..vv>>.>...>.>..v>.v....v..>...v..>>.v...v.vv>vvv.>
..>.v>..v>>v>>v>v>>.>>.>.>.v>..v>.>vv.>v..>.v>>.....>...>>v.>v..v..v...>.>....v...>v..v.>>.v>....>.v....>.>.v.v..>.....v>..v...v>.v>v.v.>..
v.>.vv...>vv.>v.>.>v.>>>.v>>v..>>>..v..>..v.>>..>....>v>v>vv..v>vv>.v....>..>>v.>>>..>>>>..>.v..v..>v..>.vv>.v>>>.v........vvv.>..v>>...v..
v.>>>.>....>.>.v>v..>..v.>.>v..>v>.v>v.>v.>.vvv>v..>.>>>>.>>>....>...>..vv..vvv..>.v.v>.>vv>...v...vvv.>..v>v>.>.>...v.>.vv.vv.v.v>.....>.>
v..>....v>.vv.>>...>vv..>..>>>.v.v.>>>>v..>v>v>v>vv.>...>>>v>.>v>.>..>vv...v.v>vv.>...>..>>..>.v>v...>..v>....vv>...>.>v.v.vv>v.>vv..>>.>..
...v..>v....>>.>>.>vv.....v>.>.vv>.v.>.v>v.>..vv...v.v.>...v.vvv....v>vv...>...>.........>.>...v.v.>.v.vv.vv.>.>...>vvvv>v..>....>>>>.v.>>>
v>>.>>vvv.....v.v>..v.>>..v..>vvv....vv>......v.>....v>v.>v.v...v...v>vv...v.>.>>..v.>v.>>v>.vv.>>v.v...v.....v>>v.v>>....>>.v>...vvvv.v.vv
..v>vv>>>>>.v>>vv..vvvv..v>>v.>v.v>.v>>......>...>.vv..>>...>.v>v..>vv..>.v..v....>.v..>>v>v...>.v...>.v>>v..vvv.>v>..>...>v.>..v>.>v>>>>>.
>.>vv..v...v>>>vv.>>v..>....v>>v.>.....v......vvv..v....>>v>....>..v....>>>>..>v..>..>.v>...>..v.v.>v>>v.v>>>...>...>v....v..>.>v>>>.vv..>.
.>.>..vv>.v>vv.>>..v.>>>>..v..>.v>>..>>.>....>....v..>..>>>v>.vvv.>v.>>>>.>>.v>v>>>..>......>>...v>vvv..>..>..>.v.vv>.>vvvv>vv.>v>vv.>.vv>v
v>.>.>v..v>v.>....v..v.v>...v.>.vv...>..>..>..>.v.>...v.>....>.>..>..vv>.>>.>.v>..v...>>..>>..>.>..vv>.v>vv.>.....v.>.....v.>.>v..v...>..>>
..v>>....v>....>v.v.v.>..v>.vv.v>.......v.>>..>...>>>.>...>..v.vv.>>>vvv.>....>.>.>>..vv....>>>..v..vvv..>>.....>>>v..v.v..>.vv.v.v.vv.v..v
>.v.v...>.v..v>>...>.vvv>>..v...v..v.v..>>.vv>>v>v...>..v>.vv..vv.vvv.v.>v..v.>>>v.v>vv..v.>>v.>>v.>>v..>.v.>.....>>v..>v.>...>....>>vv>.v.
.vv>..>>>.>..>..>>>v>v>..v..v.>.>v..v.v.>..v...v>>...v>>.v>.>>.>v.>>v>>.>.>.>v.>.>vv...v.>>>>.vv...>>>..>.v..v.vv>>...>.....vv.>>vv.....v..
>..>v.>..>>>vvvv...vv...>v....v..>.v...v>v...>>vv>v....vv.>..vv..>.>>vv.v.>>....v>v..v.v>v>..v>.v.>.>...>.>.>..vv.>>.>>>>.v..vv.....>>.v...
vv..v.>.>>vv>v>..>..v.v....v..v>........>.>..>.........>..>v>.v.>>....>>>.>vv.v..>......v.>v>>...v.>.>.>.>v>..>..>...v>>.>>.v..>...>v.v.v.>
v>..vv.>>>.vv.......>.v.>...>..>>..vv..>.v..>v..v>.v>.>.v>v.>>v..>..>>.......>v.....v.v....vv.v>......v.v>v...vvv...vvvv..>v.v..v.v...>v.>>
>..>v>.........>v...>v..>..v.>vv>.v>v>>.vv.v>..v..v>.v.vv..>>vv..v.>>>v>..vv...v..v>vv......>>..v..>.>..v>..>v...>...v.v>...>...v>>>.v.>>..
.....>...v..v..>..v.....>..>>.....vv.....>..v>..vv>.>.vvv.vv>.....v.>.v.v.v.>>v....v.vv>v.v>..vv>.>.v>>>...>.>.>..>v....vv>.>..v.>.vv>>v>>v
..v.........>.v...>..>.v.v.>v..vv...v....vv.v.>.v...vv.....>..>>>.>..v>..>.>>v.>...>..>....v>..v.>>>..>.v>vv>v>.>....vv.v....v>.vv>.v>>.>.>
.v..v..v>...v.>...v..v......v.>>.>.>v..v>.vv.......v..v>v..>>>...>v...v...>v.vv.>>.>.>...>.v.v>>.>.>>v>>.>..vv.v...>>v...>>>.>....>>>.v>v>.
v>.v..v.v>vvv.v..vvv.>...vvv.vvvvv>>.vv.>>>.v..v.>.....v>vvvv...v>...>...>v.v>.....vv>v>v.v>>.v..v.v...>v...>v>..vv>.>>..v...>>v>.>.vv..vv.
.vvv..v>....v.v>>.>...>v.vv...>>...vvvv.....vv>.....>..>.v.>.>.v.>>>v>v>.>>v...v>v>vvv>v>v>v.v>>.....>.v>vv.>>.>.v..>.>.....v.v>>......>.>.
.vv.>.>.v.v>.v>vv>>v.>>.>.vvv>v..v.vv>..v>v..v>>>>>.....>..>..v>v.v......v>.v...vv>v.>..v>.>.v>..vv..>>>....>>.>.>v...v.>>.>>..>v>.v..v.v>.
.v...>.vv>>>..v.>>.v..>>.>..v.>.>..v>>...>>...vvvvv>v..>>vvv..v.>v>......>>v>.v..v....>.>>....>>..>.>v...vv...>.v>>..>>.>....v....vv...>v..
>...>>>..>v.......v..>>>v.>>....>>.v.>>v.v>.v...v...>..>v.vvv....v.>.v>..>vvv..>..>..>vv>..vv..>>..>.v.>>v.>.>>.v>....v.>...>v...>.>..>...>
vv>...>....v..>.>..>>......>vv.v.v.>v.v.v>.>.v>.>vv.v..v>v>...>>..>....v...>v.>.v.>v.>v..>>.vvv.vvvvvv...v.vvv.vvvv.>>..vv>vv....vv.v.>>...
...>...v.>.>..v..>vv..vv>v>....vv.vv>.v....vv>.>>...v>>>..>..vv.v..v.vv.>vv>v.>v.v.>.>.v>v.v.........v>...>v.>>..v..vv>>>.v>.v.v.>.v>v>..>>
..>..>>...>>..v>vv>..>>>v.....v..v...vv....v>.....>.v...vv...>...>..>....v.vv.>v..>v....>>..>v.>vvv>v..v>...>....v>v>>v.v..vv>>.v...v>....v
.v..>...vvv.>...v..vvvvvvv.>v......vvv>v..v..v..>>v>v.v.vv....v>>..>>v.>.v.>...vv..>..>.v.v.>v>>>...>>>v..v.v.v..v>.v.>.>..>>...v..v>>>vv..
>vv..v>vvv>.>.vv...v..>.vvv..>>>....vv>..v.>.........>v>...>.v..vvv..>v..>.......v..>v..v..v>.>.v>>>vv...>>..>...vv>>>..>>..>.vv..vv>...>..
.v>vv.v..v>>>>v..v.vv>..>>>..>..>.>....>..>..v.v>....>.>v..>v.>vvv..>..>..>v....>...>..>..>.>>.vvv.v.v...v.>...v>.>v.>>vvvv.v....>v.>.v..vv
v>v.vvvv..v>vv.>v.>>.>.>>>>>v>.v>...vv>.vv.>vv>.v..>v.>>>>vv>.>>..>v.>.vvv.>>>.v>....vvv>.>..v.v..>.v>v.>..v.>.v>v..>..v>v>.>v..>v.>v...v.>
v>v..vv.vvv...>v>v.>>.v..>.>...>v.v>>>v....>>.>>v.vvvvv.vvv.>...>..>v..>>.v.vv...v>..>>>v.....>.>..>>.........>..v.v>..v..>>..v>.>vv>.>v...
...>.>.>.vv.>v..v.v.>>...v.>>....>.>.v...>..v.v..v..>vv>.>v...v>v>..>>v..vvvvv>>v.v....>v.v.>....>.>.>...v...v...v>v....v>.v.v.>>>v>>...>.v
...>>v>v.vvvv.>>>.>>>....>v>v..vvvv.v..>vvv.....>.>...v....v.vv>...v>v>>>>....v>>.>.....vv>>.v.>v.vv.>>>vv..v>>..v>...>..vv.v>v...>>.v....v
.vvv>v....>v>.>vv>.vv>>..v...>....v.>>>>>..v.>v.>.v>>.v..vv>..v....>...v.>v.>>..>.vvv.....>>..v>.>...v>v>v.vv.v.>.........v>>v...>.>>v.v>.v
>v.>vv.>.v.>.v..>>.>v....>v....vvvvv>.>vv>v.vvvv..>>>.>>v>.>.>v>v......v>>..>>...>>...>>vv.>.v.>...v>..v.>>>.....vv.>v.v>.>vv>...v>vv>.v>>.
>..>...>vv..vv.v...vvvv..>v..>.v.>.v>..>v..>......vv...>v....>.vv>vv...>v.v..>..v>.........>>>>>........>......>.vv>....>>>.>>.>v.>..v.>>.v
.>..v>v.v.vv.>..vv...>.>..>.v>.v..>>.v..>v.vv>>...>v>v.v..>v>.v.>..v.>...>.>>.v>.v.>....>v>..>>......vv.v..>vvvvv.>>v>vv>..v>.>v>.>v...>.vv
"""


def get_input() -> List[str]:
    return raw_input.split("\n")[1:-1]
