# https://judge.softuni.org/Contests/Practice/Index/1049#7

size = float(input())
input_metric = input().lower()
output_metric = input().lower()

if input_metric == "m":
    size /= 1
elif input_metric == "mm":
    size /= 1000
elif input_metric == "cm":
    size /= 100
elif input_metric == "mi":
    size /= 0.000621371192
elif input_metric == "in":
    size /= 39.3700787
elif input_metric == "km":
    size /= 0.001
elif input_metric == "ft":
    size /= 3.2808399
elif input_metric == "yd":
    size /= 1.0936133

if output_metric == "m":
    size *= 1
elif output_metric == "mm":
    size *= 1000
elif output_metric == "cm":
    size *= 100
elif output_metric == "mi":
    size *= 0.000621371192
elif output_metric == "in":
    size *= 39.3700787
elif output_metric == "km":
    size *= 0.001
elif output_metric == "ft":
    size *= 3.2808399
elif output_metric == "yd":
    size *= 1.0936133

print(size)
