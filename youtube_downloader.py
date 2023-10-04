
# Replace 'video_url' with the URL of the YouTube video you want to download
# video_url = 'https://youtu.be/g2XwkCfnoKY?si=kCz4oYG7gGZCLtie'

from pytube import YouTube

# Replace 'your_video_url' with the actual URL of the YouTube video you want to download
video_url = 'https://youtu.be/g2XwkCfnoKY?si=kCz4oYG7gGZCLtie'

# Create a YouTube object
yt = YouTube(video_url)

# Get available video streams
streams = yt.streams.filter(file_extension='mp4', progressive=True)

# Create a dictionary to store available resolutions and corresponding stream objects
available_resolutions = {}
for stream in streams:
    resolution = f"{stream.resolution} ({stream.filesize / (1024 * 1024):.2f} MB)"
    available_resolutions[resolution] = stream

# Print available resolutions and sizes
print("Available Resolutions:")
for i, resolution in enumerate(available_resolutions.keys(), start=1):
    print(f"{i}. {resolution}")

# Ask the user to choose a resolution
while True:
    try:
        choice = int(input("Enter the number of your desired resolution (or 0 to exit): "))
        if choice == 0:
            print("No, I don't wish to download")
            break
        elif 1 <= choice <= len(available_resolutions):
            break
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# If the user chose to download
if choice != 0:
    # Get the user's chosen stream
    chosen_resolution, chosen_stream = available_resolutions[choice]

    # Specify the output path for the downloaded video
    output_path = 'C:\\Users\\Dell\\Desktop'  # Replace with your desired output path

    # Provide a message to indicate that the download is starting
    print(f'Downloading video in {chosen_resolution}...')

    # Download the video
    chosen_stream.download(output_path=output_path)

    # Provide a message to indicate that the download is complete
    print('Video downloaded successfully!')

