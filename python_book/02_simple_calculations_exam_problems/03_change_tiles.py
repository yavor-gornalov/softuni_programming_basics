# https://judge.softuni.org/Contests/Practice/Index/1048#2

playground_side = int(input())
tile_length = float(input())
tile_width = float(input())
bench_length = int(input())
bench_width = int(input())

playground_area = playground_side ** 2
bench_area = bench_width * bench_length
playground_area -= bench_area

tile_area = tile_width * tile_length

tiles_count = playground_area / tile_area
tiles_time = tiles_count * 0.2

print(f"{tiles_count}\n{tiles_time}")
