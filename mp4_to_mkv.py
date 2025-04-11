import ffmpeg

input_file = "input.mp4"
output_file = "output.mkv"

ffmpeg.input(input_file).output(output_file).run()
print("Conversion complete!")
