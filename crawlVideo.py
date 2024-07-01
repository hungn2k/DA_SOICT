import subprocess

def record_rtsp_stream(rtsp_url, duration, output_file):
    try:
        # RTSP stream
        command = [
            'ffmpeg',
            '-i', rtsp_url,
            '-t', str(duration),
            '-c', 'copy',
            output_file
        ]
        

        subprocess.run(command, check=True)
        print(f"Recording saved to {output_file}")
        
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    rtsp_url = "rtsp://Cam1:Etcop@2023Ai1@cam8ocd.cameraddns.net:556/Streaming/Channels/1"
    duration = 30  # Duration in seconds
    output_file = "../video/night_output.mp4"
    
    record_rtsp_stream(rtsp_url, duration, output_file)
